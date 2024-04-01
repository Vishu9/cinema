import pytest
from django.urls import reverse
from django.test import Client
from .models import Movie
from datetime import datetime

@pytest.mark.django_db
def test_create_movie(client: Client):
    url = reverse("api:create_movie")
    data = {
        "name": "Test Movie",
        "protagonists": "John Doe",
        "start_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "coming_up",
    }

    response = client.post(url, data)
    assert response.status_code == 200
    assert response.json() == {"message": "Movie created successfully"}

@pytest.mark.django_db
def test_list_movies(client: Client):
    # Create some sample movies for testing
    Movie.objects.create(
        name="Movie 1",
        protagonists="John Doe",
        start_date=datetime.now(),
        status="coming_up",
    )
    Movie.objects.create(
        name="Movie 2",
        protagonists="Jane Smith",
        start_date=datetime.now(),
        status="starting",
    )

    url = reverse("api:list_movies")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == Movie.objects.count()
