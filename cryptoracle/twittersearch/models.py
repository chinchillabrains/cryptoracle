from django.db import models
from .customfields import BatchedValuesField

# date
# tweets
# Temporarily save batches of tweets to get sentiment later & delete
class Tweets(models.Model):
    date = models.DateField()
    tweets = BatchedValuesField(token='-splitweets-') # Something unique as token to split tweets