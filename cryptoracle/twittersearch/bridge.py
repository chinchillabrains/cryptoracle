# bridge to connect with twitter using its API
import os
import requests

def get_tweets(search_term):
    # query = 'https://api.twitter.com/2/tweets/search/recent?query={} lang:en -is:retweet&max_results=10'.format(search_term)
    # Do we need requests.utils.quote to format request before sending?
    query = 'https://api.twitter.com/2/tweets/search/recent?query={} lang:en -is:retweet&max_results=10'.format(requests.utils.quote(search_term))
    return twitter_request(query)

# Returns tweet counts for search_term in the last 7 days in 1-hour intervals
def get_tweet_counts(search_term):
    query = 'https://api.twitter.com/2/tweets/counts/recent?query={} lang:en -is:retweet'.format(search_term)
    return twitter_request(query)

def twitter_request(query):
    bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
    result = requests.get(query, headers={"Authorization": "Bearer " + bearer_token})
    return result.json()
