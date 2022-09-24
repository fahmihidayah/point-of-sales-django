from django.test import TestCase
from . import base_test
from order_item_app.models import OrderItem
from transaction_app.repositories import TransactionRepository
from transaction_app.models import Transaction


class TransactionRepositoryTest(base_test.BaseSetupTest):

    def setUp(self) -> None:
        super(TransactionRepositoryTest, self).setUp()
        self.transaction_repository : TransactionRepository = TransactionRepository()

    def test_create_transaction_true(self):
        transaction: Transaction = self.transaction_repository.create_transaction(self.user)
        self.assertEqual(transaction.total, 100)

    def test_order_item_transaction_equal_true(self):
        transaction: Transaction = self.transaction_repository.create_transaction(self.user)
        order_item = OrderItem.objects.get(pk=self.order_item.pk)
        self.assertEqual(transaction.pk, order_item.transaction.pk)

    def test_failure_craete_transaction_true(self):

        transaction: Transaction = self.transaction_repository.create_transaction(self.user)
        order_item = OrderItem.objects.get(pk=self.order_item.pk)

        new_transaction = self.transaction_repository.create_transaction(self.user)
        self.assertIsNone(new_transaction)





