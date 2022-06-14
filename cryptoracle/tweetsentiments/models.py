from django.db import models
from cryptoprices.models import Crypto

class Sentiments(models.Model):
    coin = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    date = models.DateField()
    keywords = models.CharField(max_length=100)
    sentiment = models.DecimalField(max_digits=7, decimal_places=6)
    search_volume = models.IntegerField()
    polarization = models.DecimalField(max_digits=7, decimal_places=6)