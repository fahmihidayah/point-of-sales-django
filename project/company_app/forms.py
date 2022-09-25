from django import forms
from . import models

class CompanyForm(forms.ModelForm):

    class Meta:
        model = models.Company
        fields = ['image', 'name', 'description']