from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ErrorDetail


def get_message_error(error_data : dict) -> str:
    message = ""
    for key in error_data:
        error : ErrorDetail = error_data[key][0]
        message = error.title()
        break
    return message

class RestAPIFormatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request : HttpRequest):
        path = request.path
        print('log path ' + path + ' ' + request.content_type + ' header ' + str(request.headers))
        if 'api' in request.path:
            response : Response = self.get_response(request)
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                response.data = {
                    "message" : get_message_error(response.data),
                    "error" : True,
                    "code" : response.status_code,
                    "details" : None
                }
                response._is_rendered = False
                response.render()
                return response
            return response
        else:
            return self.get_response(request)
