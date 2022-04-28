from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users', include('users.urls')),
        path('products', include('products.urls')),
    ]))
]
