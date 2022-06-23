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



    def test_build_query(self):
        inputOutput = [
            {
                'in': {
                    'service': 'search-recent',
                    'term': 'bitcoin',
                    'params': {
                        'max_results': '10',
                        'next_token': 'asyS_A_ASGDH',
                        'start_time': '2022-08-19',
                        'end_time': '2022-08-17',
                    },
                },
                'out': 'https://api.twitter.com/2/tweets/search/recent?query="bitcoin" lang:en -is:retweet&max_results=10&next_token=asyS_A_ASGDH&start_time=2022-08-19&end_time=2022-08-17'
            }
        ]
        bridge = Bridge()
        for testCases in inputOutput:
            query = bridge.build_query(service = testCases['in']['service'], term = testCases['in']['term'], params = testCases['in']['params'])
            self.assertEquals(query, testCases['out'])

        
    
    # def get_tweets():
    #     pass

    # def get_tweet_counts():
    #     pass