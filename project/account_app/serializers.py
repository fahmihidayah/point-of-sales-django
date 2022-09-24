from rest_framework import serializers
from .models import ModelBackend, UserModel, Profile


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()


class CreateUserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False, read_only=True)
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()

    def is_valid(self, raise_exception=False):
        valid = super(CreateUserSerializer, self).is_valid(raise_exception)
        if UserModel.objects.filter(email=self.initial_data['email']).count() != 0 and valid:
            raise serializers.ValidationError({"email" : "email already used"})
        if Profile.objects.filter(phone=self.initial_data['phone']).count() != 0 and valid:
            raise serializers.ValidationError({"phone" : "phone already used"})
        return valid

    def create(self, validated_data):
        super(CreateUserSerializer, self).create()
        user = UserModel.objects.create_user(email=validated_data['email'], username=validated_data['email'],
                                        password=validated_data['password'], first_name=validated_data['name'])
        profile = Profile.objects.create(user=user, phone=validated_data['phone'])
        return user
