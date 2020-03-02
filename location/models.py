from django.db import models
from movie.models import Movies
from shop.models import Client

# Create your models here.

class MoviesRent(models.Model):
    fk_movie = models.ForeignKey(Movies , null=True , on_delete=models.CASCADE)
    fk_client = models.ForeignKey(Client , null=True , on_delete=models.CASCADE)
    date_out = models.DateTimeField(null=True)
    date_return = models.DateTimeField(null=True)