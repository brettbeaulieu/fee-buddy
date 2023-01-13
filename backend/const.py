# margin lending rates
lend_rate = 0.0049

# cross margin max borrow
cross_max_btc = 26
cross_max_eth = 514
cross_max_usdt = 143000

# isolated margin max borrow
iso_max_btc = 35
iso_max_eth = 700
iso_max_usdt = 200000

# Source Indices (get_candles)
OPEN = 1
CLOSE = 2
HIGH = 3
LOW = 4

# maintenance margin rates (max leverage; max quote; max base)
btc_iso_mmr = [
    [10, 20000, 3],
    [8.91, 40000, 6],
    [8.05, 60000, 9],
    [7.36, 80000, 12],
    [6.79, 100000, 15],
    [6.31, 120000, 18],
    [5.91, 140000, 21],
    [5.57, 160000, 24],
    [5.26, 180000, 27],
    [5, 200000, 35],
]

eth_iso_mmr = [
    [10, 20000, 60],
    [8.91, 40000, 120],
    [8.05, 60000, 180],
    [7.36, 80000, 240],
    [6.79, 100000, 300],
    [6.31, 120000, 360],
    [5.91, 140000, 420],
    [5.57, 160000, 480],
    [5.26, 180000, 540],
    [5, 200000, 700],
]
