from django.contrib import admin
from .models import Category
from .forms import CategoryForm

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    form = CategoryForm

