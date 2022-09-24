from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField
from .models import Category

class CategorySerializers(ModelSerializer):

    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'created_at', 'updated_at']
