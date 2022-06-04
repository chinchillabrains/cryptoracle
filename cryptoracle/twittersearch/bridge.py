# bridge to connect with twitter using its API
import os
import requests

def get_tweets(search_term):
    query = 'https://api.twitter.com/2/tweets/search/recent?query={}&max_results=10'.format(search_term)
    return twitter_request(query)



def get_tweet_counts(search_term):
    query = 'https://api.twitter.com/2/tweets/counts/recent?query={}'.format(search_term)
    return twitter_request(query)

def twitter_request(query):
    bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
    result = requests.get(query, headers={"Authorization": "Bearer " + bearer_token})
    return result.json()
