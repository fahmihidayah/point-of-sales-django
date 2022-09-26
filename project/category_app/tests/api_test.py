from . import base_setup_test
from rest_framework.test import APIRequestFactory
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient


class ApiTestCase(base_setup_test.CategoryBaseTestCase):

    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()
        self.client: Client = Client()

    def test_token_not_none(self):
        self.assertIsNotNone(self.token)

    def test_list_api_success(self):
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.get(reverse("api_v1_list_create_category"), format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_api_success(self):
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.post(reverse("api_v1_list_create_category"),
                                   data={"name": "test", "description": "ABC"}, format='json')
        self.assertEqual(response.status_code, 200)
