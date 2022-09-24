from django.test import TestCase
from .base_setup_test import BaseSetupTest


class ModelTestCase(BaseSetupTest):

    def test_product_exist_true(self):
        self.assertIsNotNone(self.product)
