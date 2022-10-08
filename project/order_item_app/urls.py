from django.urls import path

from . import apis

urlpatterns = [

    path('api/v2/order_items', apis.OrderItemListCreateAPIView.as_view(), name='api_v2_order_item_list_create'),
    path('api/v2/order_item/<int:pk>', apis.OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='api_v2_order_item_retrieve_update_delete'),
    path('api/v1/create_order_item', apis.CreateOrderItemAPIView.as_view(),
         name='api_create_order_item'),

    # path('api/v1/order_item', apis.ListOrderItemAPIView.as_view(),
    #      name='api_list_order_item'),

    # path('api/v2/order_item', apis.ListOrderItemV2APIView.as_view(),
    #      name='api_list_order_item'),

    # path('api/v1/update_order_item/<int:pk>', apis.UpdateOrderItemOrderItemAPIView.as_view(),
    #      name='api_update_order_item'),

    # path('api/v1/delete_order_item/<int:pk>', apis.DeleteOrderItemAPIView.as_view(),
    #      name='api_delete_order_item'),

]
