from rest_framework.test import APITestCase, APIClient


class BasicTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
