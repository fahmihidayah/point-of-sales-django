from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product, models
from .serializers import ProductSerializer, ProductWriteSerializer
from .repositories import ProductRepository
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_utils import success_create, success_retrieve, success_update, success_delete
from rest_framework import status
from rest_framework.response import Response


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    product_repository: ProductRepository = ProductRepository()

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return super(ProductRetrieveUpdateDestroyAPIView, self).get_serializer_class()
    #     else:
    #         return ProductWriteSerializer
    #
    # def get_serializer(self, *args, **kwargs):
    #     if self.request.method == 'PATCH':
    #         kwargs['user'] = self.request.user
    #     return super(ProductRetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        company = self.request.user.company_set.first()
        if company:
            return self.product_repository.find_by_company(company=company)
        else:
            return self.product_repository.find_by_company(company=None)

    def delete(self, request, *args, **kwargs):
        return success_delete(
            response=super(ProductRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)
        )

    def update(self, request, *args, **kwargs):
        return success_update(
            response=super(ProductRetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs))

    def retrieve(self, request, *args, **kwargs):
        return success_retrieve(
            response=super(ProductRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs))


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    product_repository: ProductRepository = ProductRepository()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return super(ProductListCreateAPIView, self).get_serializer_class()
        else:
            return ProductWriteSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            kwargs['user'] = self.request.user
        return super(ProductListCreateAPIView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):

        company = self.request.user.company_set.first()
        if company:
            return self.product_repository.find_by_company(company=company)
        else:
            return self.product_repository.find_by_company(company=None)

    def list(self, request, *args, **kwargs):
        return success_retrieve(response=super(ProductListCreateAPIView, self).list(request, *args, **kwargs))

    def create(self, request, *args, **kwargs):
        return success_create(response=super(ProductListCreateAPIView, self).create(request, *args, **kwargs))


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return success_retrieve(super(ProductListAPIView, self).list(request, *args, **kwargs))
