from . import base_test_case
from product_app.repositories import ProductRepository

class RepositoryTestCase(base_test_case.BaseProductTestCase):

    def setUp(self) -> None:
        super(RepositoryTestCase, self).setUp()
        self.product_repository : ProductRepository = ProductRepository()

    def test_find_by_company_size_one(self):
        self.assertEqual(1, self.product_repository.find_by_company(self.company).count())
