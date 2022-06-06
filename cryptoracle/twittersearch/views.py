from django.shortcuts import render
from django.http import HttpResponse
from . import bridge
from .search import search_tweets
from .search import count_tweets

import json

# Create your views here.
def home(request):
    # tweet_counts = bridge.get_tweet_counts('bitcoin')
    tweet_counts = bridge.get_tweets('bitcoin')
    ret_str = json.dumps(tweet_counts)
    # ret_str = "\n".join(search_tweets('bitcoin'))
    return HttpResponse(ret_str)
