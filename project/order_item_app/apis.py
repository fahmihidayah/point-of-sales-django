from . import models
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_utils import success_create, success_retrieve, success_delete,success_update
from . import serializers
from .repositories import OrderItemRepository
from product_app.repositories import ProductRepository

repository: OrderItemRepository = OrderItemRepository()


class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WriteOrderItemSerializer
    order_item_repository: OrderItemRepository = OrderItemRepository()
    product_repository: ProductRepository = ProductRepository()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ReadOrderItemSerializer
        else:
            return super(OrderItemRetrieveUpdateDestroyAPIView, self).get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        if self.request.method != 'GET':
            kwargs['user'] = self.request.user
        return super(OrderItemRetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        company = self.request.user.company_set.first()
        if company:
            return self.order_item_repository.find_by_company(company=company)
        else:
            return self.order_item_repository.find_by_company(company=None)

    def update(self, request, *args, **kwargs):
        return success_update(super(OrderItemRetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs))

    def delete(self, request, *args, **kwargs):
        return success_delete(super(OrderItemRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs))

    def retrieve(self, request, *args, **kwargs):
        return success_retrieve(super(OrderItemRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs))


class OrderItemListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.WriteOrderItemSerializer
    order_item_repository: OrderItemRepository = OrderItemRepository()
    product_repository: ProductRepository = ProductRepository()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ReadOrderItemSerializer
        else:
            return super(OrderItemListCreateAPIView, self).get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            kwargs['user'] = self.request.user
            kwargs['company'] = self.product_repository.get_by_id(id=self.request.data['product']).company
        return super(OrderItemListCreateAPIView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        company = self.request.user.company_set.first()
        if company:
            return self.order_item_repository.find_by_company(company=company)
        else:
            return self.order_item_repository.find_by_company(company=None)

    def list(self, request, *args, **kwargs):
        data_total = repository.get_order_items_and_total(self.request.user)
        queryset = self.filter_queryset(data_total['order_items'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data_total['order_items'] = queryset

        return success_retrieve(Response(data=serializers.ReadOrderItemWithTotalSerializer(data_total).data))

    def create(self, request, *args, **kwargs):
        return success_create(super(OrderItemListCreateAPIView, self).create(request, *args, **kwargs))


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
