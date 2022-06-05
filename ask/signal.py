from django.contrib.auth import user_logged_in, user_logged_out,get_user_model
from notifications.signals import notify
#from django.db.models.signals import user_sign_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
#from .views import *

@receiver(post_save, sender=User)
def user_sign(sender,instance,created,**kwargs):
       if created:
         #sender=User.objects.get(username=request.user)
         #sender=User.objects.get(username=request.user)
   
         notify.send(instance, recipient=instance, verb='Welcome to Fatwa Community')
            
            
            
@receiver(post_save, sender=User)        
def Creation(sender,instance,created, **kwargs):
    if created:
        newprofile=Profile(user=instance)
        newprofile.save()

#post_save.connect(user_sign_in, sender=user_logged_in)