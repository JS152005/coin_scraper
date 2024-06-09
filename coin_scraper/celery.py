from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_scraper.settings')

app = Celery('coin_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Add a task to check the health of the Celery worker
@app.task(bind=True)
def health_check(self):
    return {'status': 'ok'}

# Add a task to scrape coin data
from.tasks import scrape_coin_data
app.register_task(scrape_coin_data)