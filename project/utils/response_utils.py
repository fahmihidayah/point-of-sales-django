from rest_framework.response import Response as ApiResponse
from rest_framework import status
DEFAULT_SUCCESS_RESPONSE = {
    'message' : "Success Retrieve Data",
    'error' : False,
    'code' : 200
}

DEFAULT_FAILURE_RESPONSE = {
    'message' : 'Failed Retrieve Data',
    'error': True,
    'code' : 400
}

DETAILS = 'details'

MESSAGE = 'message'

ERROR = 'error'

CODE = 'code'

MESSAGE_SUCCESS_RETRIEVE = "Success Retrieve Data"

MESSAGE_SUCCESS_CREATE = "Success Create Data"

MESSAGE_SUCCESS_UPDATE = "Success Update Data"

MESSAGE_SUCCESS_DELETE = "Success Delete Data"


def success_retrieve(response: ApiResponse) -> ApiResponse:
    return wrap_api_response(response, message=MESSAGE_SUCCESS_RETRIEVE)


def success_create(response: ApiResponse) -> ApiResponse:
    return wrap_api_response(response, message=MESSAGE_SUCCESS_CREATE)


def success_update(response: ApiResponse) -> ApiResponse:
    return wrap_api_response(response, message=MESSAGE_SUCCESS_UPDATE)


def success_delete(response: ApiResponse) -> ApiResponse:
    return wrap_api_response(response, message=MESSAGE_SUCCESS_DELETE)


def wrap_api_response(response: ApiResponse, message: str= MESSAGE_SUCCESS_RETRIEVE) -> ApiResponse:
    response_dict = DEFAULT_SUCCESS_RESPONSE.copy()
    response_dict[DETAILS] = response.data
    response_dict[CODE] = response.status_code
    response_dict[MESSAGE] = message
    return ApiResponse(data=response_dict)


def wrap_success(data) -> ApiResponse:
    return wrap_data(data=data, code=200)

def wrap_failure(data, message : str) -> ApiResponse:
    response_dict = DEFAULT_FAILURE_RESPONSE.copy()
    response_dict[DETAILS] = data
    response_dict[CODE] = 400
    response_dict[MESSAGE] = message
    return ApiResponse(data=response_dict, status=status.HTTP_400_BAD_REQUEST)

def wrap_data(data, code, message: str = MESSAGE_SUCCESS_RETRIEVE) -> ApiResponse:
    response_dict = DEFAULT_SUCCESS_RESPONSE.copy()
    response_dict[DETAILS] = data
    response_dict[CODE] = code
    response_dict[MESSAGE] = message
    return ApiResponse(data=response_dict)
