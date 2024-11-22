import json
from channels.generic.websocket import AsyncWebsocketConsumer



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user =  self.scope['user']
        print(self.user)
        print(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'user_join',
                'message': f"has joined the room "
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    async def send_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def user_join(self,event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message':message
        }))

    async def add_room(self,event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message':message
        },ensure_ascii=False))

    async def add_task(self, event):
        message = event['message']
        print(self.user)
        await self.send(text_data=json.dumps({
            'message': message
        }, ensure_ascii=False))