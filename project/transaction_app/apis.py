from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import repositories
from . import models

from utils.response_utils import wrap_success,wrap_failure,success_retrieve

from rest_framework.permissions import IsAuthenticated, IsAdminUser

transaction_repository : repositories.TransactionRepository = repositories.TransactionRepository()

class CreateTransactionAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        transaction : models.Transaction = transaction_repository.create_transaction(user=request.user)

        if transaction:
            serializer : serializers.TransactionSerializer = serializers.TransactionSerializer(data=transaction)

            if serializer.is_valid():
                return wrap_success(data=serializer.data)
            else:
                return wrap_failure(data={}, message='Can not create transaction')
        else:
            return wrap_failure(data={}, message='Can not create transaction, no item on cart')


class TransactionListAPIView(ListAPIView):
    transaction_repository: repositories.TransactionRepository = repositories.TransactionRepository()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TransactionSerializer

    def get_queryset(self):
        return transaction_repository.find_by_user(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(TransactionListAPIView, self).list(request, *args, **kwargs)
        return success_retrieve(response)


class TransactionDetailAPIView(APIView):
    transaction_repository: repositories.TransactionRepository = repositories.TransactionRepository()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, **kwargs):
        transaction = transaction_repository.get_by_id(kwargs['pk'])
        serializer : serializers.TransactionDetailSerializer = serializers.TransactionDetailSerializer(transaction)
        return Response(data=serializer.data)

