from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields



# Create your models here.

class Movies(models.Model):
    name = models.CharField(null=True , max_length=100)
    description = models.CharField(null=True , max_length=100)
    date = models.DateTimeField(null=True)
    thumb = models.ImageField(null=True)
    actors = models.CharField(null=True , max_length=100)
    country = models.CharField(null=True , max_length=100)
    length = models.IntegerField(null=True)
    rented = models.BooleanField(null=True , blank=True)
    director  = models.CharField(null=True , max_length=100, verbose_name=_("réalisateur"))
    def __str__(self):
        return self.name

class MovieGenre(models.Model):
    label = models.CharField(max_length = 50, null=True)
    category = models.ForeignKey(Movies , null=True , on_delete=models.CASCADE)