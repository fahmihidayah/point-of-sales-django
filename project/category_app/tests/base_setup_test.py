from django.test import TestCase
from category_app.models import Category
from category_app.repositories import CategoryRepository
from company_app.models import Company
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CategoryBaseTestCase(TestCase):

    def setUp(self) -> None:
        self.user = UserModel.objects.create(email='fahmi@emai.com', username='fahmi', password='123123123')
        self.company = Company.objects.create(name='test', description='test desc', user=self.user)
        self.category : Category = Category.objects.create(name='food', description='foof desc', company=self.company)
        self.category_repository : CategoryRepository = CategoryRepository()

