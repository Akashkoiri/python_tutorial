from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        
        self.accept()

        z

    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = json_data['message']

        # Sending the data to frontend
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))


    def disconnect(self, code):
        pass
        