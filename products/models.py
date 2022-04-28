from django.db import models
from django.core import validators


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[validators.MinValueValidator(0)])
    quantity_in_stock = models.IntegerField(validators=[validators.MinValueValidator(0)])

    class Meta:
        db_table = 'products'
