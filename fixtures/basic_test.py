from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from fixtures import factories


class BasicTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user: User = factories.UserFactory.create()
        cls.jwt_response = cls.client.post(
            reverse('users-login'),
            data={'username': cls.user.username, 'password': factories.user_password},
            format='json',
        )
