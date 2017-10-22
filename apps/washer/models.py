from django.db import models
from django.contrib.auth.models import User


class ExUserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    is_washer = models.BooleanField(default=True)
 
    def __unicode__(self):
        return self.user



from registration.signals import user_registered
 
def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_washer = bool(True)
    profile.save()
 
user_registered.connect(user_registered_callback)

# from registration.signals import user_registered
 
# def user_registered_callback(sender, user, request, **kwargs):
#     profile = ExUserProfile(user = user)
#     profile.is_human = bool(request.POST["is_human"])
#     profile.save()
 
# user_registered.connect(user_registered_callback)

