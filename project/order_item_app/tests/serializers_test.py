from .base_setup_test import BaseSetupTest, OrderItem
from django.http.request import QueryDict
from order_item_app.serializers import WriteOrderItemSerializer


class SerializersTestCase(BaseSetupTest):

    def test_is_valid_write_order_item_serializer_true(self):
        query_dict : QueryDict = QueryDict(query_string='', mutable=True)
        query_dict.update({
            'product': self.product.pk,
            'amount': 1,
        })
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data=query_dict)
        self.assertTrue(serializer.is_valid())

    def test_save_write_order_item_serializer_success(self):
        query_dict: QueryDict = QueryDict(query_string='', mutable=True)
        query_dict.update({
            'product': self.product.pk,
            'amount': 1,
        })
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data=query_dict)
        self.assertTrue(serializer.is_valid())
        order_item : OrderItem = serializer.save()
        self.assertIsNotNone(order_item)

    def test_update_order_item_success(self):
        query_dict: QueryDict = QueryDict(query_string='', mutable=True)
        query_dict.update({
            'product': self.product.pk,
            'amount': 1,
        })
        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data=query_dict)

        serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, initial=query_dict)

        self.assertEqual(3, self.order_item.amount)
    # def test_save_order_item_success(self):
    #     serializer: WriteOrderItemSerializer = WriteOrderItemSerializer(user=self.user, data={
    #             'product': self.product.pk,
    #             'amount': 1,
    #         })
    #     self.assertTrue(serializer.is_valid())
    #     self.assertEqual(1, self.order_item_repository.find_all().count())
    #
