# from project.order_item_app.repositories import OrderItemRepository
from .base_setup_test import BaseSetupTest, OrderItem

class OrderItemRepositoryTestCase(BaseSetupTest):


    def test_list_order_item_is_1(self):
        self.assertEqual(1, self.order_item_repository.find_all().count())

    def test_total_order_item_exist(self):
        order_item: OrderItem = self.order_item_repository.get_by_id(id=self.order_item.pk)
        self.assertIsNotNone(300, order_item.total)

    def test_query_by_product_and_user(self):
        self.assertIsNotNone(self.order_item_repository.get_by_product_and_user(self.product.id, self.user.id))

    def test_create_product(self):
        new_order_item: OrderItem = self.order_item_repository.create(self.product_two.pk,
                                                           self.user.pk,
                                                           1)
        new_order_result: OrderItem = self.order_item_repository.get_by_product_and_user(self.product_two.pk, self.user.pk)
        self.assertEqual(self.product_two.pk, new_order_result.product.pk)


    def test_update_product(self):
        self.order_item_repository.create(self.product_two.pk, self.user.pk, 1)
        self.order_item_repository.create(self.product_two.pk, self.user.pk,1)
        new_order_result: OrderItem = self.order_item_repository.get_by_product_and_user(self.product_two.pk, self.user.pk)
        self.assertEqual(2, new_order_result.amount)


    def test_find_all_by_user(self):
        results = self.order_item_repository.find_all_by_user_as_list(user=self.user)
        self.assertEqual(1, len(results))

    def test_first_by_user_and_company_success(self):
        order_item = self.order_item_repository.first_by_user_and_company(user=self.user, company=self.company)
        self.assertIsNotNone(order_item)

    def test_first_by_user_success(self):
        order_item = self.order_item_repository.first_by_user(user=self.user)
        self.assertIsNotNone(order_item)
