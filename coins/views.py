from django.forms import model_to_dict
from django.shortcuts import render

from coins.models import Coin
from coins.utils import create_initial_coins


def index(request):
    if not Coin.objects.exists():
        create_initial_coins()

    coins_list = [
        {**model_to_dict(coin), "price": coin.price.normalize()}
        for coin in Coin.objects.all()
    ]

    context = {"coins": coins_list}

    return render(request, "index.html", context)
