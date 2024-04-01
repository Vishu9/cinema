from celery import shared_task
from datetime import timedelta
from django.utils import timezone
import time

@shared_task
def update_movie_ranks():
    time.sleep(15)    
    print("task executing")
    # Importing models inside the task function to avoid AppRegistryNotReady error
    from .models import Movie
    
    
    movies = Movie.objects.filter(status__in=["coming_up", "starting", "running"])
    print("movie object", movies)
    for movie in movies:
        movie.ranking += 10
        movie.save()

        

# celery -A cinema worker --loglevel=info

# celery -A cinema beat --loglevel=info

