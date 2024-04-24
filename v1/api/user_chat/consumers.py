from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django.contrib.auth import get_user_model
from .models import Message
import jwt

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        auth_header = [header[1] for header in self.scope['headers'] if header[0] == b'authrization']
        if auth_header:
            token = auth_header[0].decode('utf-8').split()[1]
            print("\n#################################\n",token,"\n#################################\n")
             # Decode the JWT token
            decoded_token = jwt.decode(token)
            print("\n#################################\n",decoded_token,"\n#################################\n")
            if self.data.is_authenticated:
                self.room_name = 'chat_room'
                self.room_group_name = f'chat_{self.room_name}'

                # Join room group
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )

                self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            # Leave room group
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']

        # Save message to the database
        if self.user.is_authenticated:
            sender = self.user
            receiver_username = text_data_json.get('receiver_username')
            receiver = User.objects.get(username=receiver_username)
            message = Message.objects.create(
                sender=sender, receiver=receiver, content=message_content)

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message_content,
                    'username': sender.username,
                }
            )
        else:
            print("Error: This user is not authenticated")

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))