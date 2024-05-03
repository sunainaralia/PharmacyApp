from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
import json
from channels.db import database_sync_to_async
from .models import Chat, Group

class ChatConsumer(AsyncWebsocketConsumer):
     async def websocket_connect(self,event):
          print("websocket_connect",event)
          self.group_name = self.scope['url_route']['kwargs']['group_name']
          group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
          if not group:
            await database_sync_to_async(Group.objects.create)(
                name=self.group_name
            )
     
          await self.channel_layer.group_add(
               self.group_name ,   # Group Name
               self.channel_name
               )
          await self.send({
               "type":"websocket.accept",
          })

     async def websocket_receive(self,event):
          print("websocket_receive",event['text'])
          data = json.loads(event['text'])
          # find group name
          group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
          # Save new Chat
          chat = Chat(
               group=group,
               content=data['msg']
               )
          await database_sync_to_async(chat.save)()
          
          await self.channel_layer.group_send(
               self.group_name , # Group Name
               {
               'type':"chat.message",
               'message':event['text']
               },
          )
     
     async def chat_message(self,event):
          await self.send({
               "type":"websocket.send",
               "text":event['message']
          })
    
     async def websocket_disconnect(self,event):
          print("websocket_disconnect",event)
          await self.channel_layer.group_discard(
               self.group_name ,   # Group Name
               self.channel_name
               )
          raise StopConsumer()