# interface to use twittersearch package
# get input and return tweets & tweet volume using bridge.py
import re
from . import bridge

def search_tweets(keyword, next_token=None):
    recent_tweets = bridge.get_tweets(keyword, 10, next_token)
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

def count_tweets(keyword):
    recent_tweet_counts = bridge.get_tweet_counts(keyword)
    return recent_tweet_counts['data']