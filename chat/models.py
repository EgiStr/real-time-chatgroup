from django.db import models
from django.contrib.auth.models import User
from user.models import Usercostumer
# Create your models here.

class Chat_log(models.Model):
    user = models.ForeignKey(Usercostumer, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    class Meta:
        ordering=['timestamp']
        
    def __str__(self):
        return self.user.username 