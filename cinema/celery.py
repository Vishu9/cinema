
import os
from celery import Celery
# from django.conf import settings
# import cinema.settings as settings
# from datetime import timedelta
# from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema.settings")

app = Celery('cinema')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
#     'update-movie-ranks-every-5-minutes': {
#         'task': 'movies.tasks.update_movie_ranks',
#         'schedule': timedelta(minutes=5),
#     },
# }
