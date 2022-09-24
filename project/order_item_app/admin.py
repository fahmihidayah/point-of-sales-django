from django.contrib import admin
from . import models
from . import forms

# Register your models here.

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    form = forms.OrderItemForm
    list_display = ['product', 'amount', 'user', 'created_at', 'updated_at']
    search_fields = ['product', 'amount', 'user']
