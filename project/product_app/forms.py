from . import models
from django.forms.models import ModelForm


class ProductForm(ModelForm):

    class Meta:
        model = models.Product
        fields = ['name', 'description', 'image', 'stock', 'price', 'categories']