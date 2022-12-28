from django.urls import path
from .consumers import *



websocket_patterns = [
    path('ws/socket/', ChatConsumer.as_asgi()),
]

