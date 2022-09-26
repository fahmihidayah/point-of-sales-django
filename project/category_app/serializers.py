from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, ValidationError
from .models import Category


class CategoryReadSerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'created_at', 'updated_at']


class CategorySerializers(ModelSerializer):

    def __init__(self, **kwargs):
        super(CategorySerializers, self).__init__(**kwargs)
        self.user = None
        self.company = None

    def is_valid(self, raise_exception=False):
        is_valid = super(CategorySerializers, self).is_valid(raise_exception=raise_exception)

        if not self.user:
            raise ValidationError({'user' : 'require user data'})
        self.company = self.user.company_set.first()
        if is_valid and not self.company:
            raise ValidationError({'company': 'Current user has no company'})


        return is_valid

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data['name'], description=validated_data['description'],
                                           company=self.company)

        return category

    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'created_at', 'updated_at']
