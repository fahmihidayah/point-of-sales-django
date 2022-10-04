from .base_test_case import BaseProductTestCase
from product_app.serializers import ProductSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
# from project.product_app.serializers import ProductSerializer
from product_app.models import Product
from PIL import Image
import io

class SerializerTestCase(BaseProductTestCase):

    def setUp(self) -> None:
        super(SerializerTestCase, self).setUp()

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

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
            print(prod_new.name)
            self.assertIsNotNone(prod_new)

