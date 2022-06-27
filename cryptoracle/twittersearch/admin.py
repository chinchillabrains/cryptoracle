from django.contrib import admin
from .models import Tweets, Tweetcounts

admin.site.register(Tweets)
admin.site.register(Tweetcounts)