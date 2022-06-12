from cryptoprices.models import Crypto

coins = [
    {
        'id'        : 'bitcoin',
        'nicename'  : 'Bitcoin',
        'symbol'    : 'btc',
    }
]

for coin in coins:
    new_crypto = Crypto(id=coin['id'], nicename=coin['nicename'], symbol=coin['symbol'])
    new_crypto.save()