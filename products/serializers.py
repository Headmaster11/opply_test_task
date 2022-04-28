from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import transaction

from products.models import Product
from users.models import UserOrder

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductOrderSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(quantity_in_stock__gt=0))
    amount = serializers.IntegerField(min_value=1)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    @transaction.atomic()
    def create(self, validated_data) -> UserOrder:
        instance = UserOrder.objects.create(**validated_data)
        product = validated_data['product']
        if validated_data['amount'] > product.quantity_in_stock:
            raise ValidationError('incorrect amount')
        product.quantity_in_stock -= validated_data['amount']
        product.save()
        return instance
