from django.db import models

# prices table
    # - crypto (slugs like bitcoin)
    # - date
    # - price
    # - currency (Add later. Work with bitcoin for start)

class Prices(models.Model):
    crypto  = models.CharField(max_length=55) #53 is the max id length of available coins in coingecko
    date    = models.DateField()
    price   = models.DecimalField(max_digits=10, decimal_places=10) # Just to be safe
    