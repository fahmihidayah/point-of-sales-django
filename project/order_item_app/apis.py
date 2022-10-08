from . import models
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_utils import success_create, success_retrieve, success_delete
from . import serializers
from .repositories import OrderItemRepository

repository: OrderItemRepository = OrderItemRepository()


class OrderItemListCreateAPIView(ListCreateAPIView):
    serializers = serializers.WriteOrderItemSerializer
    order_item_repository : OrderItemRepository = OrderItemRepository()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ReadOrderItemSerializer
        else:
            return super(OrderItemListCreateAPIView, self).get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            kwargs['user'] = self.request.user
        return super(OrderItemListCreateAPIView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        company = self.request.user.company_set.first()
        if company:
            return self.order_item_repository.find_by_company(company=company)
        else:
            return self.order_item_repository.find_by_company(company=None)

    def list(self, request, *args, **kwargs):
        return super(OrderItemListCreateAPIView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(OrderItemListCreateAPIView, self).create(request, *args, **kwargs)


class ListOrderItemV2APIView(ListAPIView):
    serializer_class = serializers.ReadOrderItemSerializer
    queryset = repository.find_all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        data_total = repository.get_order_items_and_total(self.request.user)
        queryset = self.filter_queryset(data_total['order_items'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data_total['order_items'] = queryset

        return success_retrieve(Response(data=serializers.ReadOrderItemWithTotalSerializer(data_total).data))


class ListOrderItemAPIView(ListAPIView):
    serializer_class = serializers.ReadOrderItemSerializer
    queryset = repository.find_all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return success_retrieve(super(ListOrderItemAPIView, self).list(request, *args, **kwargs))


class CreateOrderItemAPIView(CreateAPIView):
    serializer_class = serializers.WriteOrderItemSerializer
    queryset = repository.find_all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        kwargs['user'] = self.request.user
        serializer: serializers.WriteOrderItemSerializer = super(CreateOrderItemAPIView, self).get_serializer(*args,
                                                                                                              **kwargs)
        return serializer

    def create(self, request, *args, **kwargs):
        return success_create(super(CreateOrderItemAPIView, self).create(request, *args, **kwargs))


class UpdateOrderItemOrderItemAPIView(UpdateAPIView):
    serializer_class = serializers.WriteOrderItemSerializer
    queryset = repository.find_all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        kwargs['user'] = self.request.user
        serializer: serializers.WriteOrderItemSerializer = super(UpdateOrderItemOrderItemAPIView, self).get_serializer(
            *args,
            **kwargs)
        return serializer

    def update(self, request, *args, **kwargs):
        return success_create(super(UpdateOrderItemOrderItemAPIView, self).update(request, *args, **kwargs))


class DeleteOrderItemAPIView(DestroyAPIView):
    serializer_class = serializers.WriteOrderItemSerializer
    queryset = repository.find_all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return success_delete(super(DeleteOrderItemAPIView, self).delete(request, *args, **kwargs))
