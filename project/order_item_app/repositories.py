from .models import OrderItem
from django.db.models import Manager, QuerySet, Q, Sum, F


class OrderItemRepository:

    def __init__(self):
        self.manager: Manager = OrderItem.objects
        self.default_query_set: QuerySet = self.manager.select_related('product').annotate(
            total=F('product__price') * F('amount')).filter(transaction_id__isnull=True)

        self.simple_query_set: QuerySet = self.manager.select_related('product').annotate(
            total=F('product__price') * F('amount'))

    def count(self, user):
        return self.find_all_by_user(user).count()

    def get_order_items_and_total(self, user):
        data_total = self.get_total_cart(user)
        data_total['order_items'] = self.find_all_by_user(user)
        return data_total

    def get_total_cart(self, user):
        result = self.default_query_set.filter(Q(user__pk=user.pk)).aggregate(
            total=Sum(F('product__price') * F('amount')))
        if not result['total']:
            result['total'] = 0
        return result

    def find_all_by_user(self, user) -> QuerySet:
        return self.default_query_set.filter(Q(user__pk=user.pk))

    def find_all_by_user_as_list(self, user):
        return self.find_all_by_user(user).values()

    def find_all(self) -> QuerySet:
        return self.default_query_set.all()

    def get_by_id(self, id) -> OrderItem:
        try:
            return self.default_query_set.get(pk=id)
        except OrderItem.DoesNotExist:
            return None

    def get_by_product_and_user(self, product_id, user_id) -> OrderItem:
        try:
            return self.default_query_set.get(Q(product__id=product_id) & Q(user__id=user_id))
        except OrderItem.DoesNotExist:
            return None

    def create(self, product_id, user_id, amount) -> OrderItem:
        order_item: OrderItem = self.get_by_product_and_user(product_id, user_id)
        if order_item:
            order_item.amount += amount
            order_item.save()
            return order_item
        else:
            return self.manager.create(product_id=product_id, user_id=user_id, amount=amount)
