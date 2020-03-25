from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from six import with_metaclass

from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from linguist.models.base import Translation



# Create your models here.
# Our Post model decider
class MovieTranslation(Translation):
    class Meta:
        abstract = False

class MovieManager(LinguistManagerMixin, models.Manager):

    pass

class Movies(with_metaclass(LinguistMeta, models.Model)):
    name = models.CharField(null=True , max_length=100)
    description = models.CharField(null=True , max_length=100)
    date = models.DateTimeField(null=True)
    thumb = models.ImageField(null=True)
    actors = models.CharField(null=True , max_length=100)
    country = models.CharField(null=True , max_length=100)
    length = models.IntegerField(null=True)
    rented = models.BooleanField(null=True , blank=True)
    director  = models.CharField(null=True , max_length=100, verbose_name=_("réalisateur"))
    objects = MovieManager()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        linguist = {
            'identifier': 'movie',
            'fields': ('description' ,'name'),
            'default_language': 'fr',
            'decider': MovieTranslation,
        }

class MovieGenre(models.Model):
    label = models.CharField(max_length = 50, null=True)
    category = models.ForeignKey(Movies , null=True , on_delete=models.CASCADE)