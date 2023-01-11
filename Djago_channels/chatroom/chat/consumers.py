import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache


CACHE_INDEX = 0


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        global CACHE_INDEX
        self.room_name = 'room1'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

        # Getting all the data from cache
        self.author = 'Akash'
        cache.key_prefix = self.author

        lst = [f'{i}' for i in range(CACHE_INDEX)]
        self.messages = cache.get_many(lst)

        if len(self.messages) > 0:
            for msg in self.messages:
                data = {
                    'type': 'chat_message',
                    'message': self.messages[msg],
                    'author': self.author
                } 
                await self.send(text_data=json.dumps(data))
         




    async def receive(self, text_data):
        global CACHE_INDEX
        json_data = json.loads(text_data)
        message = str(json_data['message'])
        author = str(json_data['username'])
        # Storing in cache
        # cache.set(author, message)
        cache.key_prefix = author
        cache.set(str(CACHE_INDEX), message)
        CACHE_INDEX += 1

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


