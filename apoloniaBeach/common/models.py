from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from apoloniaBeach.choices import DocumentChoices
from apoloniaBeach.houses.models import House
from apoloniaBeach.validators import file_validator

UserModel = get_user_model()


class AssociationDocument(models.Model):
    title = models.CharField(
        max_length=30,
    )
    document_type = models.CharField(
        max_length=50,
        choices=DocumentChoices.choices,
    )
    file = CloudinaryField(
        'file',
        validators=[file_validator, ],
    )
    upload_date = models.DateTimeField(
        auto_now_add=True
    )
    uploaded_by = (models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    ))

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(
        max_length=30,
    )
    content = models.TextField()
    category = models.CharField(
        max_length=15,
        choices=DocumentChoices.choices,
    )
    posted_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    date_posted = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
