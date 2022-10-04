from rest_framework.serializers import ModelSerializer, RelatedField,ValidationError, ImageField
from .models import Product
from category_app.serializers import CategorySerializers


class ProductReadSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'image', 'stock', 'created_at', 'updated_at']


class ProductWriteSerializer(ModelSerializer):

    def __init__(self, **kwargs):
        super(ProductWriteSerializer, self).__init__(**kwargs)
        self.user = None
        self.company = None

    def is_valid(self, raise_exception=False):
        is_valid = super(ProductWriteSerializer, self).is_valid(raise_exception=raise_exception)

        if not self.user:
            raise ValidationError({'user': 'require user data'})
        self.company = self.user.company_set.first()
        if is_valid and not self.company:
            raise ValidationError({'company': 'Current user has no company'})
        return is_valid


    def create(self, validated_data):
        return super(ProductWriteSerializer, self).create(validated_data)

    # def create(self, validated_data):
    #     category = Product.objects.create(name=validated_data['name'], description=validated_data['description'],
    #                                        company=self.company)
    #
    #     return category

    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'image', 'stock', 'created_at', 'updated_at']


# Done this test
class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'image', 'stock', 'company', 'categories', 'created_at', 'updated_at']