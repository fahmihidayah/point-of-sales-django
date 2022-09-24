from rest_framework.generics import ListAPIView
from .models import Product, models
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_utils import success_create, success_retrieve, success_update, success_delete


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        return success_retrieve(super(ProductListAPIView, self).list(request, *args, **kwargs))

