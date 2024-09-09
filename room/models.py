import random
from django.db import models
import string
from accounts.models import *
# Create your models here.
def generate_random_id():
    let=string.ascii_letters
    num=string.digits
    return ''.join(random.choices(let+num,k=8))



class Room(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    room_id=models.CharField(max_length=8,unique=True,default=generate_random_id)
    created_at=models.DateTimeField(auto_now_add=True)
    is_done=models.BooleanField(default=False)
    members=models.ManyToManyField(User)
    admin=models.ForeignKey(User, related_name='room_admin', on_delete=models.SET_NULL,null=True,blank=True)
    def save(self,*args,**kwargs):
        super(Room,self).save(*args,**kwargs)
        if self.members.count()>0:
            if self.admin is None:
               self.admin=self.members.first()
        super(Room,self).save(*args,**kwargs)
        def __str__(self):
            return self.title