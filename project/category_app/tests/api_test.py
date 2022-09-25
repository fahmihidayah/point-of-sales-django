from . import base_setup_test

class ApiTestCase(base_setup_test.CategoryBaseTestCase):

    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()

    def test_create_api_success(self):
        pass