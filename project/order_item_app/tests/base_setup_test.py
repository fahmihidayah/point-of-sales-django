from django.test import TestCase
from order_item_app.repositories import OrderItemRepository
from order_item_app.models import OrderItem
from order_item_app.serializers import WriteOrderItemSerializer
from product_app.models import Product
from django.contrib.auth import get_user_model
from company_app.models import Company
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

class BaseSetupTest(TestCase):

    def setUp(self) -> None:
        # pass

        self.user = UserModel.objects.create(email='fahmi@emai.com', username='fahmi', password='123123123')
        self.company = Company.objects.create(name='company', description='descript of company', user=self.user)
        self.product = Product.objects.create(name='baju', description='test', price=100, stock=10, company=self.company)
        self.product_two = Product.objects.create(name='celana', description='test', price=100, stock=100, company=self.company)
        self.order_item: OrderItem = OrderItem.objects.create(product=self.product, user=self.user, amount=3, company=self.company)
        self.order_item_repository: OrderItemRepository = OrderItemRepository()

        self.token, created = Token.objects.get_or_create(user=self.user)