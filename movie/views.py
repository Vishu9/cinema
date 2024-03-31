from django.shortcuts import render
from datetime import datetime
from ninja import Router, NinjaAPI, File, Form
from .models import Movie
from ninja.files import UploadedFile


router = Router()

@router.post("/add")

def create_movie(request, name: str, protagonists: str, start_date: str, status: str, poster: UploadedFile = File(provider='files'), trailer: UploadedFile = File(provider='files')): 
     
        
    if status not in [choice[0] for choice in Movie.STATUS_CHOICES]:           
        return "Invalid status value. Please use one of the following: coming_up, starting, running, finished" 

    # create a new movie instance
    movie = Movie.objects.create(
        name=name,
        protagonists=protagonists,
        poster=poster,
        trailer=trailer,
        start_date=start_date,
        status=status
    )        

    # return a success response
    return {"message": "Movie created successfully"}             

@router.get("/list")
def list_movies(request):   
    return [
        {"id": e.id, "name": e.name, "protagonists": e.protagonists, "poster": e.poster.name, "trailer": e.trailer.name, "start_date": e.start_date, "status": e.status, "ranking": e.ranking}
        for e in Movie.objects.all()
    ]


