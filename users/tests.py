from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework import status

from fixtures.basic_test import BasicTestCase
from fixtures import factories

User = get_user_model()


class UserTests(BasicTestCase):
    def test_create_user(self):
        user_count = User.objects.count()
        data = {
            "email": "some1@email.com",
            "username": "username1",
            "password": "djfnkngdkjfnkjgn",
            "first_name": "hbkhbhb",
            "last_name": "jjgvgvjh",
        }
        response = self.client.post(
            reverse('users-list'),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_count + 1, User.objects.count())
        data = {
            "email": "some1@email.com",
            "username": "username2",
            "password": "djfnkngdkjfnkjgn",
            "first_name": "hbkhbhb",
            "last_name": "jjgvgvjh",
        }
        response = self.client.post(
            reverse('users-list'),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(user_count + 1, User.objects.count())
        data = {
            "email": "some2@email.com",
            "username": "username1",
            "password": "djfnkngdkjfnkjgn",
            "first_name": "hbkhbhb",
            "last_name": "jjgvgvjh",
        }
        response = self.client.post(
            reverse('users-list'),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(user_count + 1, User.objects.count())

    def test_login(self):
        data = {
            "username": self.user.username,
            "password": factories.user_password,
        }
        response = self.client.post(
            reverse('users-login'),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data), ['refresh', 'access'])

    def test_order_history(self):
        response = self.client.get(
            reverse('users-order-history'),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user, token=self.jwt_response.data['access'])
        response = self.client.get(
            reverse('users-order-history'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
