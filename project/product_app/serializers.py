from rest_framework.serializers import ModelSerializer, RelatedField
from .models import Product
from category_app.serializers import CategorySerializers


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'image', 'stock', 'created_at', 'updated_at']