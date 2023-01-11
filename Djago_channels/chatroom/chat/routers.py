from django.urls import path
from .consumers import *



websocket_patterns = [
    path('socket/', ChatConsumer.as_asgi()),
]

