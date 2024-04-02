from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

import json

# class ChatData(AsyncWebsocketConsumer):
#     async def connect(self):

#         self.room_name = "chat_room"
#         self.room_group_name = f"chat_group_{self.room_name}"
#         print('sadasdasdasdasdasdasd')
#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()
#         # await self.send(text_data=json.dumps({'message': 'Connected to WebSocket.'}))

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'send_to_frontend',
#                 'message': f'{message}'
#             }
#         )

#     async def send_to_frontend(self, event):
#         await self.send(text_data=json.dumps(event))

class ChatData(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f"chat_group_{self.user_id}"
        # Add the channel to the room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the channel from the room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        recipient_user_id = data['recipient_user_id']
        print('recipient_user_id', recipient_user_id)

        # Find the WebSocket group for the recipient_user_id
        recipient_channel_name = f"chat_group_{recipient_user_id}"
        print('recipient_channel_name', recipient_channel_name)
        # Send the message to the WebSocket connection of the recipient_user_id
        await self.channel_layer.group_send(
            recipient_channel_name,
            {
                "type": "chat",
                "message": message,
                "sender_user_id": self.user_id
            }
        )

    async def chat(self, event):
        recipient_user_id = event['sender_user_id']
        print(recipient_user_id,self.user_id)
        if recipient_user_id == self.user_id:
            # Don't send the message back to the sender
            # return
            await self.send(text_data=json.dumps(event))