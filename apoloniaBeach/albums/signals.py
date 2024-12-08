from cloudinary.uploader import destroy
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apoloniaBeach.albums.models import Album


@receiver(post_delete, sender=Album)
def delete_file_from_cloudinary(sender, instance, **kwargs):
    if instance.file:
        public_id = instance.photo.public_id
        destroy(public_id)


@receiver(pre_save, sender=Album)
def delete_old_file_on_update(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Album.objects.get(pk=instance.pk)
            if old_instance.photo and old_instance.photo.public_id != instance.photo.public_id:
                destroy(old_instance.photo.public_id)
        except Album.DoesNotExist:
            pass
