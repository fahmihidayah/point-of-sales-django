from django.forms import ModelForm
from . import models

class TransactionForm(ModelForm):

    class Meta:
        model = models.Transaction
        fields = ['invoice_number', 'total', 'user', 'company']