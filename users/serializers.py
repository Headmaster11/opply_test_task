from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from users.models import UserOrder

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data) -> User:
        user = User.objects.get(username=validated_data['username'])
        if not user.check_password(validated_data['password']):
            raise ValidationError('Invalid password')
        return user


class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = '__all__'
