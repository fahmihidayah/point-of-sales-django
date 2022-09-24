from django.forms import ModelForm
from . import models


class OrderItemForm(ModelForm):

    class Meta:
        model = models.OrderItem
        fields = ['product', 'amount', 'user', 'transaction']