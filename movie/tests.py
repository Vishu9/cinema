# # from django.test import TestCase

# # Create your tests here.

# from ninja.test import TestClient
# from movies.models import Movie
# from movies.tasks import update_movie_ranks

# client = TestClient(router)

# def test_create_movie():
#     response = client.post("/movies", json={"name": "Test Movie", "protagonists": "Test Protagonists", "poster": "test.jpg", "trailer": "test.com", "start_date": "2024-03-27T00:00:00Z", "status": "coming_up"})
#     assert response.status_code == 200
#     assert Movie.objects.filter(name="Test Movie").exists()

# def test_list_movies():
#     response = client.get("/movies")
#     assert response.status_code == 200
#     assert len(response.json()) == Movie.objects.count()


