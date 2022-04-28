from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, UserOrderViewSet

router = SimpleRouter()
router.register('', UserViewSet, basename='users')
router.register('orders', UserOrderViewSet, basename='user_orders')

urlpatterns = router.urls
