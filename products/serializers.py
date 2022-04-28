from rest_framework import serializers
from django.contrib.auth import get_user_model

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

    def create(self, validated_data) -> UserOrder:
        return UserOrder.objects.create(**validated_data)
