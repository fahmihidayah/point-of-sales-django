from django.urls import path
from . import apis

urlpatterns = [
    path('api/v1/category', apis.CategoryListCreateAPIView.as_view(), name='api_v1_list_create_category'),
    path('api/v1/category/<int:pk>', apis.CategoryRetrieveUpdateDeleteAPIView.as_view(), name='api_v1_get_update_delete_category'),

]