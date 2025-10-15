import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict
from django.conf import settings
from .models import Coin


channel_layer = get_channel_layer()

@shared_task
def get_coins_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    data = requests.get(
        url,
        headers={
            'x-cg-demo-api-key': settings.COINGECKO_API_KEY,
        }
    ).json()

    coins = []

    for coin in data:
        coin_obj, created = Coin.objects.get_or_create(symbol=coin['symbol'])

        coin_obj.name = coin['name']
        coin_obj.symbol = coin['symbol']

        state = 'same'

        if coin_obj.price > coin['current_price']:
            state = 'fall'
        elif coin_obj.price < coin['current_price']:
            state = 'raise'

        coin_obj.price = coin['current_price']
        coin_obj.rank = coin['market_cap_rank']
        coin_obj.image = coin['image']

        coin_obj.save()

        new_data = model_to_dict(coin_obj)
        new_data.update(
            {'state': state}
        )

        coins.append(new_data)

    async_to_sync(channel_layer.group_send)('coins', {'type': 'send_new_data', 'text': coins})
