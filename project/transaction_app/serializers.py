from rest_framework.serializers import ModelSerializer
from . import models
from order_item_app.serializers import ReadOrderItemSerializer


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = ['pk', 'invoice_number', 'total', 'user', 'created_at', 'updated_at']





class TransactionDetailSerializer(ModelSerializer):

    order_items = ReadOrderItemSerializer(many=True)

    class Meta:
        model = models.Transaction
        fields = ['pk', 'invoice_number', 'total', 'user', 'order_items', 'created_at', 'updated_at']