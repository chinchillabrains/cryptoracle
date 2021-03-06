# interface to use twittersearch package
# get input and return tweets & tweet volume using bridge.py
import datetime
import re
from . import bridge
from .bridgeoo import Bridge

def search_tweets(keyword, next_token=None, start_time=None, end_time=None):
    params = {'max_results': '100', 'next_token': next_token, 'start_time' : start_time, 'end_time': end_time}
    bridgeoo = Bridge()
    recent_tweets = bridgeoo.get_tweets(term=keyword, params=params)
    try:
        tweet_count = recent_tweets['meta'].get('result_count', 0)
    except KeyError:
        print(recent_tweets)
        return {'tweets': [], 'next_token': None}

    if tweet_count == 0:
        return {'tweets': [], 'next_token': None}

    clean_tweets = []
    for tweet in recent_tweets['data']:
        # Replace newline with space
        tweetText = re.sub(r"\n", ' ', tweet['text'])
        # Remove mentions
        tweetText = re.sub(r"@\w+", '', tweetText)
        # Remove hashtags
        tweetText = re.sub(r"#[\w_\-]+", '', tweetText)
        # Remove links
        tweetText = re.sub(r"https?\:[\w_\-\/\.]+", '', tweetText)
        clean_tweets.append(tweetText)

    next_token = recent_tweets['meta'].get('next_token', None)

    return {'tweets': clean_tweets, 'next_token': next_token}

def get_yesterdays_tweets(keyword, next_token=None):
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    yesterday_from = yesterday.strftime('%Y-%m-%dT00:00:00Z')
    yesterday_to = yesterday.strftime('%Y-%m-%dT23:59:59Z')
    return search_tweets(keyword, next_token, yesterday_from, yesterday_to)

def get_yesterdays_tweet_counts(keyword):
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    yesterday_from = yesterday.strftime('%Y-%m-%dT00:00:00Z')
    yesterday_to = yesterday.strftime('%Y-%m-%dT23:59:59Z')
    bridgeoo = Bridge()
    recent_tweet_counts = bridgeoo.get_tweet_counts(term=keyword, params={'start_time': yesterday_from, 'end_time': yesterday_to})
    return recent_tweet_counts['meta']['total_tweet_count']

def count_tweets(keyword):
    bridgeoo = Bridge()
    recent_tweet_counts = bridgeoo.get_tweet_counts(term=keyword)
    return recent_tweet_counts['data']

def search_user_tweets(username):
    user = bridge.get_user(username)
    user_id = user['data'].get('id', None)
    if user_id == None:
        return []
    
    tweets = bridge.get_user_tweets(user_id, '100')
    return tweets['data']