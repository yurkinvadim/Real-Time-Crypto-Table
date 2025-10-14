from django.shortcuts import render
import requests

from real_time_crypto_table.settings import COINGECKO_API_KEY


def index(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'

    coins = requests.get(
        url,
        headers={
            'x-cg-demo-api-key': COINGECKO_API_KEY,
        }
    ).json()

    # coins = requests.get(url).json()
    return render(request, 'index.html', context={'coins': coins})
