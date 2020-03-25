from django.db import models

# Create your models here.
class Visit_stat (models.Model):
    url = models.URLField(max_length=200)
    ip =  models.GenericIPAddressField(null=True, blank=True)
    date = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('url', 'ip', 'date')