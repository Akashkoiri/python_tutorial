# Websockets Setup

---

### 1. Settings.py

```py
INSTALLED_APPS = [
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
    'chat',
]

ASGI_APPLICATION = 'chatroom.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
```

### 2. asgi.py

```py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routers import websocket_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroom.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_patterns)
    )
})
```

### 3. routers.py

```py
from django.urls import path
from .consumers import *


websocket_patterns = [
    path('socket/', ChatConsumer.as_asgi()),
]

```

### 4. consumers.py

```py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    # Establishing a new socket connection
    def connect(self):
        self.room_name = 'room1'

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()

    # Getting data from the Frontend
    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = str(json_data['message'])
        author = str(json_data['username'])
        # Storing in cache
        # cache.set(author, message)
        cache.set(author, message)


        # Brodcasting the data to everyone on the channel_layer
        async_to_sync(self.channel_layer.group_send)(
            # Sending the below json data to this room
            self.room_name,
            {
                'type': 'chat_message',  # Create a function of this name
                'message': message,
                'author': author
            }
        )

    # This is an extra function to send the data to frontend 
    def chat_message(self, data):
        self.send(text_data=json.dumps(data))
```

### 5. consumers.py [Better version]

```py
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'room1'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()


    async def receive(self, text_data):
        json_data = json.loads(text_data)
        message = str(json_data['message'])
        author = str(json_data['username'])
        # Storing in cache
        # cache.set(author, message)
        cache.set(author, message)


        # Brodcasting the data to everyone on the channel_layer
        await self.channel_layer.group_send(
            # Sending the below json data to this room
            self.room_name,
            {
                'type': 'chat_message',  # Create a function of this name
                'message': message,
                'author': author
            }
        )


    async def chat_message(self, data):
        await self.send(text_data=json.dumps(data))
```