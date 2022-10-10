from django.contrib import admin
from .models import Transaction
from .forms import TransactionForm

# Register your models here.


@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):

    form = TransactionForm
    list_display = ['pk', 'invoice_number', 'total', 'user', 'created_at', 'updated_at']

