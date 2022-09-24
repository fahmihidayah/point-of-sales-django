from django.test import TestCase
from category_app.models import Category
from category_app.repositories import CategoryRepository

class CategoryBaseTestCase(TestCase):

    def setUp(self) -> None:
        self.category : Category = Category.objects.create(name='food', description='foof desc')
        self.category_repository : CategoryRepository = CategoryRepository()

