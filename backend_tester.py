from backend.bitget.mix.market_api import MarketApi as FuturesAPI
api = FuturesAPI("","","")

data = api.history_fund_rate("BTCUSDT" + "_UMCBL", 500, 1)["data"] 
data = [x for x in data]

print(data)