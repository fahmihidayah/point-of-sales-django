from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from . import serializers

from . import repositories


class ListConfigView(ListAPIView):
    repository : repositories.ConfigRepository = repositories.ConfigRepository()
    authentication_classes = []
    serializer_class = serializers.ConfigSerializers
    queryset = repository.default_query_set

    def list(self, request, *args, **kwargs):
        response = super(ListConfigView, self).list(request, *args, **kwargs)
        return Response(
            data={
                'message' : 'Success Retrieve',
                'code' : response.status_code,
                'error' : False,
                'details' : response.data
            }
            ,status= HTTP_200_OK
        )
