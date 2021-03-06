import factory

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from products.models import Product
from users.models import UserOrder

User = get_user_model()

user_password = 'some_password'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    username = factory.Faker('word')
    email = factory.Faker('ascii_email')
    password = factory.LazyFunction(lambda: make_password(user_password))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False
    is_superuser = False


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    quantity_in_stock = factory.Faker('pyint', min_value=0)


class UserOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserOrder

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    amount = factory.Faker('pyint', min_value=1)
