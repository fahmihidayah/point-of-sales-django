from django.urls import path
from . import apis

urlpatterns = [
    path('api/v1/create_transaction', apis.CreateTransactionAPIView.as_view(), name='api_create_transaction'),
    path('api/v1/transactions', apis.TransactionListAPIView.as_view(), name='api_list_transactions'),
    path('api/v1/transaction/<int:pk>', apis.TransactionDetailAPIView.as_view(), name='api_detail_transactions'),
]