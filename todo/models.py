from django.db import models
from room.models import *
# Create your models here.

class Todo(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    is_done=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)