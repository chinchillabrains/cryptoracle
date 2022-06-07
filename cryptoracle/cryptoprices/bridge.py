# Documentation https://github.com/man-c/pycoingecko
from pycoingecko import CoinGeckoAPI

def get_price(coin):
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=coin, vs_currencies='usd')
    return price[coin]['usd']

# e.g. coins = ['bitcoin', 'litecoin', 'ethereum']
def get_prices(coins):
    cg = CoinGeckoAPI()
    prices = cg.get_price(ids=coins, vs_currencies='usd')
    ret_prices = {}
    for coin in prices:
        ret_prices[coin] = prices[coin]['usd']
    return ret_prices