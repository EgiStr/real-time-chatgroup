from django.urls import re_path,path

from .consumers import ChatConsumer

Websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/',ChatConsumer.as_asgi())
]