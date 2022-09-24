from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


class ListConfigView(APIView):
    authentication_classes = []

    def get(self, request):
        return Response(data={
            'message': 'Success Retrieve Data',
            'code' : 200,
            'error': False,
        })