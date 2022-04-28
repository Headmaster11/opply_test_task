from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, permissions
from django.contrib.auth import get_user_model

from users.serializers import UserCreateSerializer, UserLoginSerializer, UserOrderSerializer
from users.utils import get_tokens_for_user
from users.models import UserOrder

User = get_user_model()


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ('login',):
            return UserLoginSerializer
        return UserCreateSerializer

    def create(self, request):
        data = request.data
        serializer: UserCreateSerializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(get_tokens_for_user(serializer.instance), status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False)
    def login(self, request):
        data = request.data
        serializer: UserLoginSerializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(get_tokens_for_user(serializer.instance), status.HTTP_200_OK)


class UserOrderViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserOrderSerializer

    def get_queryset(self):
        return UserOrder.objects.filter(user=self.request.user).order_by('-created_at').select_related('product')
