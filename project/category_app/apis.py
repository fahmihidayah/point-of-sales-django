from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializers, CategoryReadSerializers
from utils.response_utils import success_create, success_retrieve, success_update, success_delete
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import permissions
from . import repositories


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    category_repository : repositories.CategoryRepository = repositories.CategoryRepository()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryReadSerializers
        else:
            return super(CategoryListCreateAPIView, self).get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        serializer = super(CategoryListCreateAPIView, self).get_serializer(*args, **kwargs)
        serializer.user = self.request.user
        return serializer

    def get_queryset(self):
        # return self.category_repository.find_all()
        company = self.request.user.company_set.first()
        if company:
            return self.category_repository.find_by_company(company=company)
        else:
            return self.category_repository.find_by_company(company=None)

    def list(self, request, *args, **kwargs):
        return success_retrieve(
            response=super(CategoryListCreateAPIView, self).list(request, *args, **kwargs)
        )

    def create(self, request, *args, **kwargs):
        return success_create(
            response=super(CategoryListCreateAPIView, self).create(request, *args, **kwargs)
        )


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    category_repository : repositories.CategoryRepository = repositories.CategoryRepository()
    serializer_class = CategoryReadSerializers
    permission_classes = [IsAuthenticated, permissions.IsUserOwnerPermission]

    def get_serializer(self, *args, **kwargs):
        serializer = super(CategoryRetrieveUpdateDeleteAPIView, self).get_serializer(*args, **kwargs)
        serializer.user = self.request.user
        return serializer

    def get_queryset(self):
        # return self.category_repository.find_all()
        company = self.request.user.company_set.first()
        if company:
            return self.category_repository.find_by_company(company=company)
        else:
            return self.category_repository.find_by_company(company=None)

    def retrieve(self, request, *args, **kwargs):
        return success_retrieve(
            response=super(CategoryRetrieveUpdateDeleteAPIView, self).retrieve(request, *args, **kwargs)
        )

    def update(self, request, *args, **kwargs):
        return success_update(
            response=super(CategoryRetrieveUpdateDeleteAPIView, self).update(request, *args, **kwargs)
        )

    def delete(self, request, *args, **kwargs):
        return success_delete(
            response=super(CategoryRetrieveUpdateDeleteAPIView, self).delete(request, *args, **kwargs)
        )

