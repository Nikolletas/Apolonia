from cloudinary.uploader import destroy
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from apoloniaBeach import settings
from apoloniaBeach.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        subject = f"New User Added: {instance.email}"
        message = f"A new User has been added - {instance.first_name} {instance.last_name}."
        recipient_list = ['nikoletas@abv.bg']

        # send_email_notification.delay(subject, message, recipient_list)
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )


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


