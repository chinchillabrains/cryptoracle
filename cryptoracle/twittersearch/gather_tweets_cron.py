import datetime
from twittersearch.search import get_yesterdays_tweets
from twittersearch.search import get_yesterdays_tweet_counts
from twittersearch.models import Tweets
from twittersearch.models import Tweetcounts
from cryptoprices.models import Crypto

def gather_tweets(keyword):
    next_token = ''
    yesterday = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    while next_token != None:
        next_token = None if next_token == '' else next_token
        response = get_yesterdays_tweets(keyword, next_token)
        tweets = response['tweets']
        next_token = response['next_token']
        if len(tweets) > 0:
            # Save to db
            Tweets.objects.create(date = yesterday, tweets = tweets)

def gather_tweet_counts():
    yesterday = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    cryptos = Crypto.objects.all()
    for crypto in cryptos:
        count = get_yesterdays_tweet_counts(crypto.id)
        Tweetcounts.objects.create(date=yesterday, crypto=crypto, count=count)