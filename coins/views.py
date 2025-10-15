from django.forms import model_to_dict
from django.shortcuts import render

from coins.models import Coin


def index(request):
    coins_list = [
        {**model_to_dict(coin), "price": coin.price.normalize()}
        for coin in Coin.objects.all()
    ]

    context = {"coins": coins_list}

    return render(request, "index.html", context)
