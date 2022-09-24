from django.db import models
from category_app.models import Category
# Create your models here.
from django.utils.html import mark_safe


class Product(models.Model):

    name: models.CharField = models.CharField(max_length=255, default='')

    description: models.TextField = models.TextField(max_length=500, default='')

    image: models.ImageField = models.ImageField(upload_to='media/', blank=True)

    price: models.FloatField = models.FloatField(default=0, blank=True)

    stock: models.IntegerField = models.IntegerField(default=0, blank=True)

    categories: models.ManyToManyField = models.ManyToManyField(to=Category)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image == '':
            return mark_safe('<img src="/media/media/place-holder.png" width="150" height="150" />')
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'