from django.test import TestCase, Client
from django.urls import reverse

class UrlTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_create_order_item_200(self):
        response = self.client.get(reverse('api_order_item'))
        self.assertEqual(response.status_code, 200)

    def test_update_order_item_200(self):
        response = self.client.get(reverse('api_update_order_item', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_delete_order_item_200(self):
        response = self.client.get(reverse('api_delete_order_item', args=[1]))
        self.assertEqual(response.status_code, 200)


