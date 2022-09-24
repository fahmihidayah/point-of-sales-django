from django.contrib import admin
from . import models, forms

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    form = forms.ProductForm
    search_fields = ['name', 'description', 'stock', 'price']
    list_display = ['image_tag', 'name', 'stock', 'price', 'created_at', 'updated_at']



