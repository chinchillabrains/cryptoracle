from ast import keyword
from django.db import models
from .customfields import BatchedValuesField
from cryptoprices.models import Crypto

# date
# tweets
# keyword
# Temporarily save batches of tweets to get sentiment later & delete
class Tweets(models.Model):
    date    = models.DateField()
    keyword = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    tweets  = BatchedValuesField(token='-splitweets-') # Something unique as token to split tweets

class Tweetcounts(models.Model):
    date    = models.DateField()
    keyword = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    count   = models.IntegerField()