from django.contrib import admin
from .models import Sentiments

class SentimentsSettingsAllFields(admin.ModelAdmin):
    list_display = [field.name for field in Sentiments._meta.get_fields()]

admin.site.register(Sentiments, SentimentsSettingsAllFields)