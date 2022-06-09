from django.shortcuts import render
from django.http import HttpResponse
from . import bridge
from .search import search_tweets
from .search import count_tweets
from analyzesentiment import analyze

import json

# Create your views here.
def home(request):
    # tweet_counts = bridge.get_tweet_counts('bitcoin')
    # tweet_counts = bridge.get_tweets('bitcoin')
    # ret_str = json.dumps(tweet_counts)
    # ret_str = "\n".join(search_tweets('bitcoin')['tweets'])
    tweets_response = search_tweets('bitcoin')
    next_token = tweets_response['next_token']
    tweets = tweets_response['tweets']
    for tweet in tweets:
        print(tweet)
        print(analyze.get_text_sentiment(tweet).subjectivity)
        
    tweets_response = search_tweets('bitcoin', next_token=next_token)
    next_token = tweets_response['next_token']
    tweets = tweets_response['tweets']
    for tweet in tweets:
        print(tweet)
        print(analyze.get_text_sentiment(tweet).subjectivity)
    return HttpResponse('Done!')
