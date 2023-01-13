from datetime import datetime, timedelta
from math import ceil, floor

from PySide6.QtCore import QDate, QDateTime, QTime

import funding_utils
import const
from bitget.mix.market_api import MarketApi as FuturesAPI
from bitget.spot.market_api import MarketApi as SpotAPI


class API_Utils:
    # TODO: Sub out all UMCBL to make extensible
    # TODO: May want to pull APIs out of this class
    def __init__(self):
        self.f_api = FuturesAPI("", "", "", True, False)
        self.s_api = SpotAPI("", "", "", True, False)

    def get_tickers(self) -> set:
        """Returns a set of symbols that are available on both spot and futures"""
        futures_symbols = [x["symbol"] for x in self.f_api.tickers("umcbl")["data"]]
        futures_symbols = [x[0:-6] for x in futures_symbols]
        spot_symbols = [x["symbol"] for x in self.s_api.tickers()["data"]]
        combined_symbols = set(futures_symbols) & set(spot_symbols)
        return combined_symbols

    def get_candles(self, symbol: str, source: int, frm: datetime, dest: datetime) -> list:
        """With input symbol, and a start/end date, returns a list of candles\
            from the start to end date in the form of [[timestamp, open],...]"""
        roc = (
            timedelta(days=4, hours=4)
            if (dest - frm) > timedelta(days=4, hours=4)
            else (dest - frm)
        )
        t_dst = frm + roc

        data = []
        while frm < dest:
            ts1 = str(frm.timestamp() * 1000)[:-2]  # [:-2] to remove decimal
            ts2 = str(t_dst.timestamp() * 1000)[:-2]
            data.append(self.f_api.candles(symbol + "_UMCBL", "1H", ts1, ts2))
            if roc != timedelta(days=4, hours=4):
                break
            if t_dst + timedelta(days=4, hours=4) > dest:
                roc = dest - t_dst
            frm = t_dst
            t_dst += roc

        data = sum(data, [])
        final = [x[:1] for x in data]
        for point in final:
            point[0] = datetime.fromtimestamp(int(point[0]) / 1000)
        for index, val in enumerate(final):
            val.append(data[index][source])
        final.reverse()

        return final

    def get_funding(self, symbol: str, frm: datetime, dest: datetime, hours: list) -> list:
        """Using an input symbol, a start/end date, and funding hours, returns a\
        list of funding rates."""

        periods = funding_utils.get_funding_periods(frm, dest, hours)
        start_trim = funding_utils.get_period_distance(dest, hours)
        trim_distance = floor(start_trim / 100)  # pages size 100
        rate_series = []

        # Build rate series from requests
        if (periods + start_trim) > 100:
            iters = ceil(periods / 100)
            for page in range(trim_distance, trim_distance + iters + 1):
                rate_series += funding_utils.get_funding_page(
                    self.f_api, symbol, page + 1
                )
        else:
            rate_series += funding_utils.get_funding_page(self.f_api, symbol)

        rate_series = rate_series[start_trim : start_trim + periods]
        for rate in rate_series:
            del rate["symbol"]
            rate["settleTime"] = int(rate["settleTime"]) / 1000
            rate["settleTime"] = datetime.fromtimestamp(rate["settleTime"])

        return rate_series

    def combined_history(self, symbol: str, src: str, frm_d: datetime, dest_d: datetime) -> list:

        funding_times = funding_utils.funding_times(self.f_api, symbol)
        price_history = self.get_candles(symbol, src, frm_d, dest_d)
        price_trim = [x for x in price_history if x[0].hour in funding_times]

        times = [price[0] for price in price_trim]
        final_funding = price_trim

        fund_history = self.get_funding(symbol, frm_d, dest_d, funding_times)
        for funding_line in fund_history:
            if len(sum(final_funding, [])) == len(times) * 3:
                break
            for index, val in enumerate(times):
                if funding_line["settleTime"] == val:
                    final_funding[index].append(funding_line["fundingRate"])

        return final_funding

    def solve_fees(self, symbol: str, src: str, qty: float, frm: QDateTime, dest: QDateTime) -> list:
        frm_d = frm.toPython()
        dest_d = dest.toPython()
        combined = self.combined_history(symbol, src, frm_d, dest_d)

        return combined


if __name__ == "__main__":
    utils = API_Utils()
    
    qdate3 = QDate(2022, 12, 29)
    qtime3 = QTime(11, 0, 0)
    frm2 = QDateTime(qdate3, qtime3)
    qdate4 = QDate(2023, 1, 1)
    qtime4 = QTime(12, 0, 0)
    to2 = QDateTime(qdate4, qtime4)

    hours = funding_utils.funding_times(utils.f_api, "SOLUSDT")

    res1 = utils.get_funding("SOLUSDT", frm2.toPython(), to2.toPython(), hours)
    
    print("Bef")
    