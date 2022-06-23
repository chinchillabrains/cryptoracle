from django.test import TestCase
from .bridgeoo import Bridge

class TwitterBridgeTests(TestCase):
    # def startUp():
    #     pass

    def test_service_url(self):
        inputOutput = {
            'search-recent': 'tweets/search/recent',
            'counts-recent': 'tweets/counts/recent',
        }
        
        bridge = Bridge()
        for inVar in inputOutput.keys():
            outVar = inputOutput[ inVar ]
            searchQuery = bridge.get_service_url(inVar)
            self.assertEquals(searchQuery, outVar)



    # def test_build_query():
    #     pass
    
    # def get_tweets():
    #     pass

    # def get_tweet_counts():
    #     pass