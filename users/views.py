from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, permissions
from django.contrib.auth import get_user_model

from users.serializers import UserCreateSerializer, UserLoginSerializer
from users.utils import get_tokens_for_user

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

    @action(methods=['GET'], detail=False, permission_classes=(permissions.IsAuthenticated,))
    def order_history(self, request):
        user = request.user
        # todo business logic
        return Response()
