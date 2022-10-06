from django.urls import path
from . import apis


urlpatterns = [
    path('api/v1/products', apis.ProductListCreateAPIView.as_view(), name='api_v1_products'),
    path('api/v1/product/<int:pk>', apis.ProductRetrieveUpdateDestroyAPIView.as_view(), name='api_v1_product_detail')
]