from django.contrib import admin
from .models import Crypto
from .models import Prices

class CryptoSettingsAllFields(admin.ModelAdmin):
    list_display = [field.name for field in Crypto._meta.get_fields() if field.related_model is None]

class PricesSettingsAllFields(admin.ModelAdmin):
    list_display = [field.name for field in Prices._meta.get_fields()]

admin.site.register(Crypto, CryptoSettingsAllFields)
admin.site.register(Prices, PricesSettingsAllFields)