from symtable import Symbol
from django.db import models
    
# crypto table
    # crypto slug (primary key)
    # nicename
    # symbol
    # related_keywords (Useful keywords related to the cryptocurrency)
class Crypto(models.Model):
    id                  = models.CharField(primary_key=True, max_length=55)     # 53 is the max id length of available coins in coingecko
    nicename            = models.CharField(max_length=60)                       # 54 is the max name length of available coins in coingecko
    symbol              = models.CharField(max_length=5)                        # All big coins have 5 symbol chars max. We won't deal with small coins
    related_keywords    = models.TextField()


# prices table
    # - crypto (foreign key)
    # - date
    # - price
    # - currency (Add later. Work with bitcoin for start)
class Prices(models.Model):
    crypto  = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    date    = models.DateField()
    price   = models.DecimalField(max_digits=10, decimal_places=10) # Just to be safe
