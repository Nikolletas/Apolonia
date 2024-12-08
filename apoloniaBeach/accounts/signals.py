from cloudinary.uploader import destroy
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete, pre_save
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


@receiver(post_delete, sender=Profile)
def delete_file_from_cloudinary(sender, instance, **kwargs):
    if instance.profile_picture:
        public_id = instance.profile_picture.public_id
        destroy(public_id)


@receiver(pre_save, sender=Profile)
def delete_old_file_on_update(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Profile.objects.get(pk=instance.pk)
            if old_instance.profile_picture and old_instance.profile_picture.public_id != instance.profile_picture.public_id:
                destroy(old_instance.file.public_id)
        except Profile.DoesNotExist:
            pass


