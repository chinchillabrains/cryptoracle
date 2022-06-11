from django.shortcuts import render
from django.http import HttpResponse
from .bridge import *

# Create your views here.
def home(request):
    # coins = get_available_coins()
    # print(get_coin_history('bitcoin', '07-06-2022'))
    return HttpResponse('Done!')