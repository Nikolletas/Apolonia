from cloudinary.uploader import destroy
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from apoloniaBeach.common.models import AssociationDocument


@receiver(post_delete, sender=AssociationDocument)
def delete_file_from_cloudinary(sender, instance, **kwargs):
    if instance.file:
        public_id = instance.file.public_id
        destroy(public_id)


@receiver(pre_save, sender=AssociationDocument)
def delete_old_file_on_update(sender, instance, **kwargs):
    if instance.pk:  # Проверка дали обектът вече съществува (т.е. не е нов)
        try:
            old_instance = AssociationDocument.objects.get(pk=instance.pk)
            # Проверка дали файлът се е сменил
            if old_instance.file and old_instance.file != instance.file:
                destroy(old_instance.file.public_id)  # Изтрива стария файл от Cloudinary
        except AssociationDocument.DoesNotExist:
            pass