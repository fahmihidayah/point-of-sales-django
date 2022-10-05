from .base_test_case import BaseProductTestCase
from product_app.serializers import ProductSerializer,ProductWriteSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
# from project.product_app.serializers import ProductSerializer, ProductWriteSerializer
from product_app.models import Product
from PIL import Image
import io

class SerializerTestCase(BaseProductTestCase):

    def setUp(self) -> None:
        super(SerializerTestCase, self).setUp()


    def test_serializer_validation_true(self):
        serializer : ProductSerializer = ProductSerializer(data={
            'name' : 'prod test',
            'description' : 'description',
            'price' : 12.0,
            'image' :  SimpleUploadedFile('image.jpg', self.generate_photo_file().getvalue()),
            'stock' : 12,
            'company': self.company.pk,
            'categories': [self.category.pk]
        })
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_serializer_save_success(self):
        serializer: ProductSerializer = ProductSerializer(data={
            'name': 'Baju test',
            'description': 'description',
            'price': 12.0,
            'image': SimpleUploadedFile('image.jpg', self.generate_photo_file().getvalue()),
            'stock': 12,
            'company': self.company.pk,
            'categories': [self.category.pk]
        })

        if serializer.is_valid():
            prod_new = serializer.save()
            self.assertIsNotNone(prod_new)

    def test_product_write_serializer_valid_true(self):
        serializer : ProductWriteSerializer = ProductWriteSerializer(user=self.user, data={
            'name': 'Baju test',
            'description': 'description',
            'price': 12.0,
            'image': SimpleUploadedFile('image.jpg', self.generate_photo_file().getvalue()),
            'stock': 12,
            'categories': [self.category.pk]
        })

        self.assertTrue(serializer.is_valid())

    def test_product_write_serializer_save_success(self):
        serializer : ProductWriteSerializer = ProductWriteSerializer(user=self.user, data={
            'name': 'Baju test',
            'description': 'description',
            'price': 12.0,
            'image': SimpleUploadedFile('image.jpg', self.generate_photo_file().getvalue()),
            'stock': 12,
            'categories': [self.category.pk]
        })

        if serializer.is_valid():
            prod = serializer.save()
            self.assertIsNotNone(prod)

