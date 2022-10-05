from .base_test_case import BaseProductTestCase
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

class ApiTestCase(BaseProductTestCase):

    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()
        self.client: Client = Client()

    def test_get_list_product_success(self):
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.get(reverse("api_v1_products"), format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_create_product_success(self):
        api_client = APIClient()

        tmp_file = self.test_file()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = api_client.post(reverse("api_v1_products"),
                                   data={
                                       'name': 'Baju test',
                                       'description': 'description',
                                       'price': 12.0,
                                       'image': tmp_file,
                                       'stock': 12,
                                       'categories': [self.category.pk]
                                   },
                                   format='multipart')
        print(response.data)
        self.assertEqual(response.status_code, 201)
