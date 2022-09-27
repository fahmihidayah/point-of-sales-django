from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer

def get_message_error(error_data: dict) -> str:
    message = ""
    for key in error_data:
        error = error_data[key]
        if error is not list:
            message = error.title()
        else:
            message = error[0].title()
        break
    return message


class RestAPIFormatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        path = request.path
        print('log path ' + path + ' ' + request.content_type + ' header ' + str(request.headers))
        if 'api' in request.path:
            response: Response = self.get_response(request)
            # get_message_error(response.data)
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                response.data = {
                    "message": get_message_error(response.data),
                    "error": True,
                    "code": response.status_code,
                    "details": None
                }
                response._is_rendered = False
                response.render()
                return response
            if response.status_code == status.HTTP_403_FORBIDDEN:
                response.data = {
                    "message": get_message_error(response.data),
                    "error": True,
                    "code": response.status_code,
                    "details": None
                }
                response._is_rendered = False
                response.render()
                return response
            if response.status_code == status.HTTP_404_NOT_FOUND:
                response.data = {
                    "message": get_message_error(response.data),
                    "error": True,
                    "code": response.status_code,
                    "details": None
                }
                response._is_rendered = False
                response.render()
                return response
            return response



        else:
            return self.get_response(request)
