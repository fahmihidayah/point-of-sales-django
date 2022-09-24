from django.urls import path

from . import apis

urlpatterns = [
    path('api/v1/create_order_item', apis.CreateOrderItemAPIView.as_view(),
         name='api_create_order_item'),


    # path('api/v1/order_item', apis.ListOrderItemAPIView.as_view(),
    #      name='api_list_order_item'),

    path('api/v2/order_item', apis.ListOrderItemV2APIView.as_view(),
         name='api_list_order_item'),

    path('api/v1/update_order_item/<int:pk>', apis.UpdateOrderItemOrderItemAPIView.as_view(),
         name='api_update_order_item'),
    
    path('api/v1/delete_order_item/<int:pk>', apis.DeleteOrderItemAPIView.as_view(),
         name='api_delete_order_item'),

]
