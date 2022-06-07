from django.shortcuts import render
from django.http import HttpResponse
from .bridge import get_price
from .bridge import get_prices

# Create your views here.
def home(request):
    prices = get_prices('bitcoin,ethereum')
    print(prices)
    return HttpResponse('Done!')