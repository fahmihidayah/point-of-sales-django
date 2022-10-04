from django.test import TestCase
from django.contrib.auth import get_user_model
from product_app.models import Product
from category_app.models import Category
from company_app.models import Company
from category_app.repositories import CategoryRepository

UserModel = get_user_model()


class BaseProductTestCase(TestCase):

    def setUp(self) -> None:
        self.user: UserModel = UserModel.objects.create(username='fahmi', password='123456')
        self.company: Company = Company.objects.create(name='company', description='test', user=self.user)
        self.category: Category = Category.objects.create(name='food', description='Food', company=self.company)
        self.product: Product = Product.objects.create(name='noodle', description='test',
                                                       price=1100.0, company=self.company, stock=10)
        self.product.categories.add(self.category)

    def test_all_object_not_none(self):
        self.assertIsNotNone(self.user)
        self.assertIsNotNone(self.company)
        self.assertIsNotNone(self.category)
        self.assertIsNotNone(self.product)

    def test_category_not_none(self):
        self.assertEqual(1, self.product.categories.count())
