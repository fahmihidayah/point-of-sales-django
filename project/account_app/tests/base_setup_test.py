from django.test import TestCase
from account_app.models import UserModel, Profile


class AccountBaseSetupTestCase(TestCase):

    def setUp(self) -> None:
        self.user = UserModel.objects\
            .create(email='fahmi@gmail.com',
                    password='123456789',
                    first_name='fahmi',
                    last_name='hidayah',)
        self.profile = Profile.objects.create(user=self.user, phone='08123456789')

    def test_user_not_null_true(self):
        self.assertIsNotNone(self.user)

    def test_profile_not_null_true(self):
        self.assertIsNotNone(self.profile)