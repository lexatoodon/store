import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'report-every-day-at-11:55': {
        'task': 'order.tasks.daily_report',
        'schedule': crontab(hour=11, minute=55)
    },
}
app.conf.timezone = 'UTC'