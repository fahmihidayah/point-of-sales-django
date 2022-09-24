from django.urls import path
from . import apis


urlpatterns = [
    path('api/v1/products', apis.ProductListAPIView.as_view(), name='api_v1_products'),
]