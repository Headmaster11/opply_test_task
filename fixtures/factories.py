import factory

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

user_password = 'some_password'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    username = factory.faker.Faker('word')
    email = factory.faker.Faker('ascii_email')
    password = factory.LazyFunction(lambda: make_password(user_password))
    first_name = factory.faker.Faker('first_name')
    last_name = factory.faker.Faker('last_name')
    is_staff = False
    is_superuser = False
