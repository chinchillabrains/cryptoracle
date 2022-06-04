from django.shortcuts import render
from django.http import HttpResponse
from . import bridge

import json

# Create your views here.
def home(request):
    tweet_counts = bridge.get_tweet_counts('bitcoin')
    ret_str = json.dumps(tweet_counts)
    return HttpResponse(ret_str)
