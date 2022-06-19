import datetime
from twittersearch.search import get_yesterdays_tweets
from twittersearch.models import Tweets

next_token = ''
keyword = 'bitcoin'
yesterday = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
while next_token != None:
    next_token = None if next_token == '' else next_token
    response = get_yesterdays_tweets(keyword, next_token)
    tweets = response['tweets']
    next_token = response['next_token']
    if len(tweets) > 0:
        # Save to db
        Tweets.objects.create(date = yesterday, tweets = tweets)
