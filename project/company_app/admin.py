from django.contrib import admin
from . import models, forms
# Register your models here
@admin.register(models.Company)
class CompanyModelAdmin(admin.ModelAdmin):
    form = forms.CompanyForm
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
