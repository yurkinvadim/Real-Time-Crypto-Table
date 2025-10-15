import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_time_crypto_table.settings')

app = Celery('cmc_project')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_10s': {
        'task': 'coins.tasks.get_coins_data',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()
