from cryptoprices.models import Crypto

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