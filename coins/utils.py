import requests
from django.conf import settings

from coins.models import Coin


def create_initial_coins():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    data = requests.get(
        url,
        headers={
            'x-cg-demo-api-key': settings.COINGECKO_API_KEY,
        }
    ).json()

    for coin in data:
        Coin.objects.create(
            symbol=coin['symbol'],
            name=coin['name'],
            price = coin['current_price'],
            rank = coin['market_cap_rank'],
            image = coin['image']
        )

