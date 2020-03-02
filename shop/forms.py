from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User




ClientInlineFormSet = inlineformset_factory(User, Client,
    fields="__all__",
        exclude=(),
        can_delete=False,
        extra=1
                )



