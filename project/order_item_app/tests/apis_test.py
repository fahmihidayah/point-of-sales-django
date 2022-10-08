from .base_setup_test import BaseSetupTest
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient

class ApiTestCase(BaseSetupTest):

    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()

    def test_get_list_order_item_success(self):
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.get(reverse("api_v2_order_item_list_create"), format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_create_order_item_success(self):
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.post(reverse("api_v2_order_item_list_create"), data={
            'product' : self.product.pk,
            'amount' : 1
        }, format='json')
        self.assertEqual(response.status_code, 200)