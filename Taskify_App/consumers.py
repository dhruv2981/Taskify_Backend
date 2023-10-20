from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name='room_name'
        self.room_group_name = 'room_group_name'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps())

        pass

    def receive(self):
        # get data from frontend to backend
        pass

    def disconnect(self):
        #when consumer leave the socket
        pass
