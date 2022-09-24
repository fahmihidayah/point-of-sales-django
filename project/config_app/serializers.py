from . import models
from rest_framework import serializers

class ConfigSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Config
        fields = ['pk', 'key', 'value', 'created_at','updated_at']