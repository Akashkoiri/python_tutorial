import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routers import websocket_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroom.settings')




application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_patterns)
})