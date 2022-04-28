from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status

from fixtures.basic_test import BasicTestCase


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
