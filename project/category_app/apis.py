from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializers
from utils.response_utils import success_create, success_retrieve, success_update, success_delete
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import repositories


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    category_repository : repositories.CategoryRepository = repositories.CategoryRepository()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer_context(self):
        context = super(CategoryListCreateAPIView, self).get_serializer_context()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

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

