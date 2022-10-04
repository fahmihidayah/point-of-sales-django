from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Product, models
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_utils import success_create, success_retrieve, success_update, success_delete


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return super(ProductListCreateAPIView, self).get_serializer_class()

    def get_queryset(self):
        return super(ProductListCreateAPIView, self).get_queryset()

    def list(self, request, *args, **kwargs):
        return super(ProductListCreateAPIView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ProductListCreateAPIView, self).create(request, *args, **kwargs)

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        return success_retrieve(super(ProductListAPIView, self).list(request, *args, **kwargs))

