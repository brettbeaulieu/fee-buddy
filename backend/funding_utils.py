from datetime import datetime, timedelta
from bitget.mix.market_api import MarketApi as FuturesAPI
from math import floor

def first_funding_period(frm: datetime, hours: list) -> datetime:
    samples = [datetime(frm.year, frm.month, frm.day, x) for x in hours]
    return min([x for x in samples if x >= frm], key=lambda x: abs(x - frm))


def most_recent_funding(frm: datetime, hours: list) -> datetime:
    samples = [datetime(frm.year, frm.month, frm.day, x) for x in hours]
    return min([x for x in samples if x <= frm], key=lambda x: abs(x - frm))


def funding_times(api: FuturesAPI, symbol: str) -> list:
    first = int(api.funding_time(symbol + "_UMCBL")["data"]["fundingTime"])
    first = datetime.fromtimestamp(first / 1000)
    full = [
        first.hour,
        (first + timedelta(hours=8)).hour,
        (first + timedelta(hours=16)).hour,
    ]
    full.sort()
    return full


# The funding fee is generated every 8 hours.
# TODO: add different funding times support. sol default rn
def get_funding_periods(frm: datetime, dest: datetime, hours: list[int]) -> int:
    # Push to first funding period
    start = first_funding_period(frm, hours)
    if start>dest:
        return 0
        
    total = 1

    # Count remaining periods
    while start + timedelta(hours=8) < dest:
        start += timedelta(hours=8)
        total += 1

    # return total
    return total


def get_period_distance(dest: datetime, hours: list[int]) -> int:
    now = datetime.now()
    diff = most_recent_funding(now, hours) - most_recent_funding(dest, hours)
    return round(diff / timedelta(hours=8))


def get_funding_page(api: FuturesAPI, symbol: str, page: int = 1):
    return api.history_fund_rate(symbol + "_UMCBL", 100, page)["data"]
