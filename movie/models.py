from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    protagonists = models.TextField(null=True)
    poster = models.ImageField(upload_to='posters/', null=True)
    trailer = models.FileField(upload_to='trailers/', null=True) 
    start_date = models.DateTimeField(null=True)
    STATUS_CHOICES = (
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming_up')
    ranking = models.IntegerField(default=0)

