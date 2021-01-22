from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Usercostumer(models.Model):
    CHOICES_status = (
        ('ada' , 'ada'),
        ('busy','busy'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username= models.CharField(max_length=30,default=user)
    profil = models.ImageField(upload_to='image', height_field='height_field', width_field='width_field',default='image/default.jpg')
    bio = models.CharField(max_length=150,default='Hey aku memakai apa ini')
    status = models.CharField(max_length=20,choices=CHOICES_status,default='ada')
    width_field = models.PositiveIntegerField(default=0)
    height_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_usercostumer(sender, instance, created, **kwargs):
    if created:
        Usercostumer.objects.create(
            user=instance,
            username=str(instance.username)
        )