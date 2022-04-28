from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from fixtures import factories

User = get_user_model()


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
        factories.ProductFactory.create_batch(100)
        factories.UserOrderFactory.create_batch(10, user=cls.user)
        another_user = factories.UserFactory.create()
        factories.UserOrderFactory.create_batch(10, user=another_user)
