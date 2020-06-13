from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# We used this signals to create the profile as soon as the user is created 
# signals allows sender to notify the receiver to do some actions or to perform  

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()    
