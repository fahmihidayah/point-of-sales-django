from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, ValidationError
from .models import Category

class CategorySerializers(ModelSerializer):

    def __init__(self, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')

        super(CategorySerializers, self).__init__(**kwargs)

    def is_valid(self, raise_exception=False):
        is_valid = super(CategorySerializers, self).is_valid(raise_exception=raise_exception)

        if not self.user:
            raise ValidationError({'user' : 'require user data'})
        elif is_valid and self.user.company_set.count() == 0:
            raise ValidationError({'company': 'Current user has no company'})

        return is_valid

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data['name'], description=validated_data['description'],
                                           company=self.user.company_set.first())

        return category

    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'company', 'created_at', 'updated_at']
