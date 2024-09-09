from django.db import models
from accounts.models import *
from room.models import *
# Create your models here.

class Message(models.Model):
    title=models.CharField(max_length=150)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    member=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
