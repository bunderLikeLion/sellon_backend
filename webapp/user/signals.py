from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import User
from .models.profile import Profile
import random


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        user = instance
        n = random.randrange(1, 10)
        Profile.objects.create(user=user, image='avatars/avatar%d.png' % n)
