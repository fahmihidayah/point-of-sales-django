from .models import Transaction
from order_item_app.models import OrderItem
from order_item_app.repositories import OrderItemRepository
from django.db.models import Manager, QuerySet, Q, Sum, F, Prefetch
from datetime import datetime


class TransactionRepository:

    def __init__(self):
        self.order_item_repository: OrderItemRepository = OrderItemRepository()
        self.manager: Manager = Transaction.objects
        self.default_query_set: QuerySet = self.manager.all()

    def find_by_user(self, user) -> QuerySet:
        return self.default_query_set.filter(Q(user__pk=user.pk))

    def get_by_id(self, id) -> Transaction:
        return self.default_query_set\
            .prefetch_related(Prefetch("orderitem_set",
                                       to_attr='order_items',
                                       queryset=self.order_item_repository.simple_query_set)).get(Q(pk=id))

    def create_invoice_number(self, transaction_id):
        return datetime.now().strftime("%m%d%H%M") + str(transaction_id)

    def create_transaction(self, user):
        if self.order_item_repository.count(user=user) == 0:
            return None

        total_data = self.order_item_repository.get_total_cart(user=user)

        transaction = self.manager.create(user=user, total=total_data['total'])

        self.order_item_repository.find_all_by_user(user=user).update(transaction=transaction)

        transaction.invoice_number = self.create_invoice_number(transaction_id=transaction.pk)

        transaction.save()

        return transaction
