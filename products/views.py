from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import permissions

from products.models import Product
from products.serializers import ProductSerializer
from products.pagination import ProductPagination


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.filter(quantity_in_stock__gt=0).order_by('id')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = (permissions.IsAuthenticated,)
