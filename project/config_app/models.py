from django.db import models

# Create your models here.

class Config(models.Model):

    key : models.CharField = models.CharField(max_length=100)

    value : models.CharField = models.CharField(max_length=100)

    created_at : models.DateTimeField = models.DateTimeField(auto_now=True)

    updated_at : models.DateTimeField = models.DateTimeField(auto_now_add=True)
