from bitget.consts import CONTRACT_WS_URL
from bitget.mix.market_api import MarketApi as FuturesAPI
from bitget.spot.market_api import MarketApi as SpotAPI



fAPI = FuturesAPI("", "", "", True, False)
sAPI = SpotAPI("", "", "", True, False)
#fAPI.contracts("umcbl")
fAPI.history_fund_rate("SOLUSDT_UMCBL",40)
#sAPI.tickers()

