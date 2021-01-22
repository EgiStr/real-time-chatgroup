import json
from channels.generic.websocket import AsyncWebsocketConsumer
from user.models import Usercostumer
from .models import Chat_log
import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    async def new_massage(self,data):
        # print(usermodel)
        databaru = Chat_log.objects.create(
            user=Usercostumer.objects.get(username=data['username']),
            content =  data['message'],
            timestamp = datetime.datetime.now()
        )
       
        content = {
            'massage':[{
                'user':self.to_json_user(databaru.user),
                'message':databaru.content,
                'timestamp':str(databaru.timestamp),
            }]
        }
        await self.send_massage(content)
        
        

    async def get_lates_chat(self,data):
        massage= self.get_database()
   
        # massage = async_to_sync(self.get_database())
        content ={
            'massage':self.to_json(massage)
            }
        await self.send_lates(content)

    def get_database(self):
        return Chat_log.objects.all()

    command = {
        'send_massage':new_massage,
        'get_lates':get_lates_chat
    }

    # membuat menjadi sebuah obj 
    def to_json(self,content):
        return [{'user':self.to_json_user(c.user),'message':c.content,'timestamp':str(c.timestamp)} for c in content]

    def to_json_user(self,content):
        return {'username':content.username,'profil':content.profil.url,'status':content.status}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
       
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print(close_code)
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.command[data['command']](self,data)
        
    
        # Send message to room group
   
    async def send_massage(self,data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'massage_group',
                'message':data['massage'],
           
            }
        )
        
    async def send_lates(self,data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'massage_lates',
                'message':data['massage']
            }
        )
        

    # Receive message from room group
    async def massage_group(self, event):
      
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    async def massage_lates(self, event):
        # # Send message to WebSocket
        await self.send(text_data=json.dumps(event))