# Object-oriented bridge to connect with twitter using its API
import os
import requests

class Bridge:

    def __init__(self):
        pass

    def get_tweets(self):
        pass

    def get_tweet_counts(self):
        pass

    def build_query(self, service='search-recent', term='', params={}):
        api_base = 'https://api.twitter.com/2/'
        service_base = self.get_service_url(service)
        keyword_query = '?query="{}" lang:en -is:retweet'.format(term)
        params_str = '&'.join('{}={}'.format(key, params[key]) for key in params.keys())
        full_query = '{}{}{}&{}'.format(api_base, service_base, keyword_query, params_str)
        return full_query


    def api_get(self, query):
        bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
        result = requests.get(query, headers={"Authorization": "Bearer " + bearer_token})
        return result.json()

    def get_service_url(self, service):
        service_base = ''
        # service_after = ''
        if service == 'search-recent':
            service_base = 'tweets/search/recent'
        elif service == 'counts-recent':
            service_base = 'tweets/counts/recent'
        # elif service == 'user':
        #     service_base = 'users/by/username/'
        # elif service == 'user-tweets':
        #     service_base = 'tweets/counts/recent'
        #     service_after = '/tweets/'

        return service_base
