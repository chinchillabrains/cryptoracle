from cryptoprices.models import Crypto
from cryptoprices.models import Prices
from cryptoprices.bridge import get_coin_history
import datetime
import time

# Add coins to DB
def init_crypto_coin_data():
    coins = [
        {
            'id'        : 'bitcoin',
            'nicename'  : 'Bitcoin',
            'symbol'    : 'btc',
        },
        {
            'id'        : 'ethereum',
            'nicename'  : 'Ethereum',
            'symbol'    : 'eth',
        },
        {
            'id'        : 'solana',
            'nicename'  : 'Solana',
            'symbol'    : 'sol',
        },
        {
            'id'        : 'dogecoin',
            'nicename'  : 'Dogecoin',
            'symbol'    : 'doge',
        },
        {
            'id'        : 'litecoin',
            'nicename'  : 'Litecoin',
            'symbol'    : 'ltc',
        },
    ]

    for coin in coins:
        new_crypto = Crypto(id=coin['id'], nicename=coin['nicename'], symbol=coin['symbol'])
        new_crypto.save()

# Initial prices pull
def init_crypto_prices_data():
    coins = Crypto.objects.all()
    numdays = 365 # get last 365 days
    base_date = datetime.datetime.today()
    daterange = [base_date - datetime.timedelta(days=x) for x in range(numdays)]
    
    for coin in coins:
        for selected_date in daterange:
            time.sleep(0.5)
            price = get_coin_history(coin.id, selected_date.date().strftime("%d-%m-%Y"))
            Prices.objects.create(crypto=coin, date=selected_date, price=price)
            print(f"{coin.id}: {price} {selected_date.date().strftime('%d-%m-%Y')}")



if __name__ == 'django.core.management.commands.shell':
    init_crypto_prices_data()