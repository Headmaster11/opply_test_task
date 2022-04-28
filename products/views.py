from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status

from products.models import Product
from products.serializers import ProductSerializer, ProductOrderSerializer
from products.pagination import ProductPagination


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.filter(quantity_in_stock__gt=0).order_by('id')
    pagination_class = ProductPagination
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ('order',):
            return ProductOrderSerializer
        return ProductSerializer

    @action(methods=['POST'], detail=True)
    def order(self, request, pk):
        product = self.get_object()
        serializer: ProductOrderSerializer = self.get_serializer(data={
            'user': request.user.pk, 'amount': request.data['amount'], 'product': product.pk}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
