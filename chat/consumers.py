import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test' #انشاء كروب واعطاءه اسم  

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message_text = text_data_json['message']

        room_id = text_data_json['room']
        user_id = text_data_json['user']


        # Lazy load models to avoid import issues
        from chat.models import Message, Room
        from accounts.models import User

        try:
            user = User.objects.get(id=user_id)
            room = Room.objects.get(id=room_id)
            
        except User.DoesNotExist:
            self.send(text_data=json.dumps({
                'error': f"User with id {user_id} does not exist."
            }))
            return
        except Room.DoesNotExist:
            self.send(text_data=json.dumps({
                'error': f"Room with id {room_id} does not exist."
            }))
            return

        message = Message.objects.create(title=message_text, room=room, member=user)
        image= '/static/imgs/profile.png'
        if user.image:
            image = user.image.url
        async_to_sync(self.channel_layer.group_send)(#ارسال البيانات 
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_text,
                # 'room': room.title,
                'user': user.username,
                'image': image
            }
        )
        

    def chat_message(self, event):
        message = event['message']
        # room = event['room']
        user = event['user']
        image = event['image']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            # 'room': room,
            'user': user,
            'image': image
            
        }))





