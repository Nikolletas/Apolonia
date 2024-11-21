from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apoloniaBeach.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def deactivate_user_on_profile_delete(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.apartment.clear()
        user.is_active = False
        user.is_staff = False
        user.save()