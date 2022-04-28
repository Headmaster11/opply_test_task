from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True


class UserOrder(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'orders')
    product = models.ForeignKey('products.Product', models.CASCADE, 'users')
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_orders'
