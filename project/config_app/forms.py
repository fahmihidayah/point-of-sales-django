from django import forms
from . import models

class ConfigForm(forms.ModelForm):

    class Meta:
        model = models.Config
        fields = ['key', 'value']