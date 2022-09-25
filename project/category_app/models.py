from django.db import models
from company_app.models import Company

# Create your models here.

class Category(models.Model):

    name: models.CharField = models.CharField(max_length=200, default='')

    description: models.TextField = models.TextField(max_length=200, default='')

    company: models.ForeignKey = models.ForeignKey(to=Company, default=None, null=True, on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
