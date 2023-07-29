from django.dispatch import receiver
from .models import User
from django.db.models.signals import post_save
from applications.accounts.managers.services import UserProfileService


@receiver(post_save, sender=User)
def create_user(sender, instance, created:bool, **kwargs):
    if created:
        UserProfileService.create_user_profile(data={"user": instance})
