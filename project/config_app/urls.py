from django.urls import path
from . import apis


urlpatterns = [
    path('api/v1/config', apis.ListConfigView.as_view(), name='api_list_config'),
]