from .base_setup_test import AccountBaseSetupTestCase
from account_app.repositories import UserRepository
from account_app.serializers import CreateUserSerializer

class SerializerTestCase(AccountBaseSetupTestCase):

    def setUp(self) -> None:
        super(SerializerTestCase, self).setUp()
        self.user_repository : UserRepository = UserRepository()

    def test_valid_user_and_profile_true(self):
        serializer : CreateUserSerializer = CreateUserSerializer(data={
            "email": "fahmi.test@gmail.com",
            "phone": "0812311111",
            "password": "123456789",
            "name": "fahmi test"
        })
        self.assertTrue(serializer.is_valid())

    def test_create_user_and_profile_success(self):
        serializer: CreateUserSerializer = CreateUserSerializer(data={
            "email": "fahmi.test@gmail.com",
            "phone": "0812322222",
            "password": "123456789",
            "name": "fahmi test"
        })
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            self.assertIsNotNone(self.user_repository.find_by_id(id=user.pk))

    def test_valid_user_and_profile_phone_false(self):
        serializer: CreateUserSerializer = CreateUserSerializer(data={
            "email": "fahmi.test@gmail.com",
            "phone": "08123444444",
            "password": "123456789",
            "name": "fahmi test"
        })
        if serializer.is_valid():
            serializer.create(serializer.validated_data)

        serializer: CreateUserSerializer = CreateUserSerializer(data={
            "email": "fahmi.test.123@gmail.com",
            "phone": "08123444444",
            "password": "123456789",
            "name": "fahmi test"
        })
        self.assertFalse(serializer.is_valid())

