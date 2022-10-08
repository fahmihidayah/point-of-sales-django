from . import models
from rest_framework.serializers import ModelSerializer, FloatField, SlugRelatedField, RelatedField, \
    PrimaryKeyRelatedField, Serializer, ValidationError
from django.http import QueryDict
from product_app.serializers import ProductSerializer
from product_app.models import Product
from .repositories import OrderItemRepository

order_item_repository : OrderItemRepository = OrderItemRepository()


class WriteOrderItemSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.user = None
        self.company = None
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
            self.company = self.user.company_set.first()
            kwargs['data']['user'] = self.user.pk
            if self.company:
                kwargs['data']['company'] = self.company.pk

        super(WriteOrderItemSerializer, self).__init__(*args, **kwargs)

    def is_valid(self, raise_exception=False):
        is_valid = super(WriteOrderItemSerializer, self).is_valid(raise_exception=raise_exception)

        if not self.user:
            raise ValidationError({'user': 'require user data'})
        self.company = self.user.company_set.first()
        if is_valid and not self.company:
            raise ValidationError({'company': 'Current user has no company'})
        return is_valid

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
        fields = [ 'product', 'amount', 'user', 'company', 'created_at', 'updated_at']


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

