from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class Company(models.Model):

    image: models.ImageField = models.ImageField(upload_to='company/')

    name: models.CharField = models.CharField(max_length=100)

    user: models.ForeignKey = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    description: models.TextField = models.TextField(max_length=500)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)