from django.urls import re_path
from .consumers import ProjectConsumer

websocket_urlpatterns = [
    re_path(r'ws/some_path/$',ProjectConsumer.as_asgi()),
]
