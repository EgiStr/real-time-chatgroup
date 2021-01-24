from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import tree
from user.models import Usercostumer
# Create your models here.



class Group_room(models.Model):
    room_name = models.CharField(max_length=30,unique=True)
    profil_group =models.ImageField(upload_to='image',default='image/default.jpg')
   

class Chat_log(models.Model):
    user = models.ForeignKey(Usercostumer, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    group = models.ForeignKey(Group_room, on_delete=models.CASCADE)

    class Meta:
        ordering=['timestamp']
        
    def __str__(self):
        return self.user.username
        