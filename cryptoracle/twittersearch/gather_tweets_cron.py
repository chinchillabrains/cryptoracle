import datetime
from twittersearch.search import get_yesterdays_tweets
from twittersearch.search import get_yesterdays_tweet_counts
from twittersearch.bridgeoo import Bridge
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

def gather_tweet_counts(past_days = 1):
    selected_date = datetime.datetime.today() - datetime.timedelta(past_days)
    date_from = selected_date.strftime('%Y-%m-%dT00:00:00Z')
    date_to = selected_date.strftime('%Y-%m-%dT23:59:59Z')
    bridgeoo = Bridge()
    cryptos = Crypto.objects.all()
    for crypto in cryptos:
        recent_tweet_counts = bridgeoo.get_tweet_counts(term=crypto.id, params={'start_time': date_from, 'end_time': date_to})
        count = recent_tweet_counts['meta']['total_tweet_count']
        Tweetcounts.objects.create(date=yesterday, crypto=crypto, count=count)