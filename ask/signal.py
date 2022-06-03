from django.contrib.auth import user_logged_in, user_logged_out
from notifications.signals import notify
#from django.db.models.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_sign_in(request, user, **kwargs):
    notify.send(user, recipient=user, verb='You sign In')
    

#post_save.connect(user_sign_in, sender=user_logged_in)