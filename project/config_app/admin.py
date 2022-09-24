from django.contrib import admin
from . import models, forms

# Register your models here.

@admin.register(models.Config)
class ConfigModelAdmin(admin.ModelAdmin):
    form = forms.ConfigForm
    search_fields = ['key', 'value']
    list_display = ['pk', 'key', 'value', 'created_at', 'updated_at']

