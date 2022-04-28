from rest_framework.reverse import reverse
from rest_framework import status

from fixtures.basic_test import BasicTestCase
from products.pagination import ProductPagination
from products.models import Product
from products.serializers import ProductSerializer


class ProductTests(BasicTestCase):
    def test_list(self):
        response = self.client.get(
            reverse('products-list'),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user, token=self.jwt_response.data['access'])
        response = self.client.get(
            reverse('products-list'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        paginator = ProductPagination()
        self.assertEqual(len(response.data['results']), paginator.page_size)
        queryset = Product.objects.filter(quantity_in_stock__gt=0).order_by('id')[:paginator.page_size]
        self.assertQuerysetEqual(response.data['results'], ProductSerializer(instance=queryset, many=True).data)

    def test_retrieve(self):
        product = Product.objects.first()
        response = self.client.get(
            reverse('products-detail', args=[product.id])
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user, token=self.jwt_response.data['access'])
        response = self.client.get(
            reverse('products-detail', args=[product.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProductSerializer(instance=product).data)
