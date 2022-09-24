from . import models
from rest_framework.serializers import ModelSerializer, FloatField, SlugRelatedField, RelatedField, \
    PrimaryKeyRelatedField, Serializer
from django.http import QueryDict
from product_app.serializers import ProductSerializer
from product_app.models import Product
from .repositories import OrderItemRepository

order_item_repository : OrderItemRepository = OrderItemRepository()



class WriteOrderItemSerializer(ModelSerializer):
    def __init__(self, instance=None, data: QueryDict = None, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')

        if data is not None:
            data._mutable = True
            data.update({
                'user': self.user.pk
            })
        super(WriteOrderItemSerializer, self).__init__(instance, data, **kwargs)

    def create(self, validated_data):
        order_item = order_item_repository.get_by_product_and_user(
            product_id=validated_data['product'].pk,
            user_id=self.user.pk
        )

        if order_item:
            return order_item_repository.create(product_id=validated_data['product'].pk,
                                                user_id=self.user.pk,
                                                amount=validated_data['amount'])
        else:
            return super(WriteOrderItemSerializer, self).create(validated_data)

    class Meta:
        model = models.OrderItem
        fields = [ 'product', 'amount', 'user',  'created_at', 'updated_at']


class ReadOrderItemSerializer(ModelSerializer):
    total = FloatField(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = models.OrderItem
        fields = ['pk', 'product', 'amount', 'total', 'user','transaction', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ReadOrderItemWithTotalSerializer(Serializer):
    total = FloatField()
    order_items = ReadOrderItemSerializer(many=True,)

