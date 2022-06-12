from django.contrib import admin
from .models import Crypto
from .models import Prices

# Register your models here.
admin.site.register(Crypto)
admin.site.register(Prices)