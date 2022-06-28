from django.contrib import admin

from .models import Tweets, Tweetcounts

class TweetsSettingsAllFields(admin.ModelAdmin):
    list_display = [field.name for field in Tweets._meta.get_fields()]

class CountsSettingsAllFields(admin.ModelAdmin):
    list_display = [field.name for field in Tweetcounts._meta.get_fields()]

admin.site.register(Tweets, TweetsSettingsAllFields)
admin.site.register(Tweetcounts, CountsSettingsAllFields)