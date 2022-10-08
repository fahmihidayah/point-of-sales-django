from .base_setup_test import BaseSetupTest, OrderItem
from django.http.request import QueryDict
from order_item_app.serializers import WriteOrderItemSerializer


class SerializersTestCase(BaseSetupTest):

    def test_is_valid_write_order_item_serializer_true(self):
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
            'product': self.product.pk,
            'amount': 1,
        })
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)

    def test_save_write_order_item_serializer_success(self):
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
            'product': self.product.pk,
            'amount': 1,
        })
        self.assertTrue(serializer.is_valid())
        order_item : OrderItem = serializer.save()
        self.assertIsNotNone(order_item)

    def test_update_order_item_success(self):
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
            'product': self.product.pk,
            'amount': 1,
        })
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
            'product': self.product.pk,
            'amount': 1,
        })
        self.assertEqual(3, self.order_item.amount)

    def test_is_valid_write_order_item_serializer_v2_true(self):
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
            'product': self.product.pk,
            'amount': 1,
        })
        self.assertTrue(serializer.is_valid())
