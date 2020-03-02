from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from userena.models import UserenaBaseProfile

# Create your models here.

class Client(UserenaBaseProfile):
    user = models.OneToOneField(User,
        unique=True,
        verbose_name=_('client_profile'),
        related_name='client',
        on_delete=models.CASCADE)