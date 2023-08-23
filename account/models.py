from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from asset_app.models import Company

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=50,blank=True, null=True)
    phone = models.CharField(max_length=13,blank=True, null=True)
    address = models.TextField(max_length=250,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile "
    
@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.Profile.save()