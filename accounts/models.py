from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(max_length=255,null=False,unique=True)
    image=models.ImageField(upload_to='profile_images',blank=True,null=True)
    name=models.CharField(max_length=150)
    REQUIRED_FIElDS=['name']