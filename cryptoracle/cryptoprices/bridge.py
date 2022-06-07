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

def get_available_coins():
    cg = CoinGeckoAPI()
    coins = cg.get_coins_list()
    return coins

# date format: dd-mm-yyyy
def get_coin_history(coin, date):
    cg = CoinGeckoAPI()
    history = cg.get_coin_history_by_id(coin, date, localization='false')
    return history['market_data']['current_price']['usd']