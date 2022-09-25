from rest_framework import serializers
from .models import ModelBackend, UserModel, Profile
from company_app.models import Company


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()


class CreateUserAndCompanySerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(min_length=8)
    password = serializers.CharField(min_length=8)
    name = serializers.CharField(min_length=3)

    company_name = serializers.CharField(min_length=8)
    company_description = serializers.CharField()

    def is_valid(self, raise_exception=False):
        valid = super(CreateUserAndCompanySerializer, self).is_valid(raise_exception)
        if UserModel.objects.filter(email=self.initial_data['email']).count() != 0 and valid:
            raise serializers.ValidationError({"email" : "email already used"})
        if Profile.objects.filter(phone=self.initial_data['phone']).count() != 0 and valid:
            raise serializers.ValidationError({"phone" : "phone already used"})
        if Company.objects.filter(name=self.initial_data['company_name']).count() != 0 and valid:
            raise serializers.ValidationError({"company_name": "Company name already used"})
        return valid

    def create(self, validated_data):
        user = UserModel.objects.create_user(email=validated_data['email'], username=validated_data['email'],
                                        password=validated_data['password'], first_name=validated_data['name'])
        profile = Profile.objects.create(user=user, phone=validated_data['phone'])
        company = Company.objects.create(user=user, name=validated_data['company_name'], description=validated_data['company_description'])
        return user

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
        user = UserModel.objects.create_user(email=validated_data['email'], username=validated_data['email'],
                                        password=validated_data['password'], first_name=validated_data['name'])
        profile = Profile.objects.create(user=user, phone=validated_data['phone'])
        return user
