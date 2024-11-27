from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from apoloniaBeach.choices import PhotoTypesChoices, CurrencyChoices
from apoloniaBeach.houses.models import Apartment
from apoloniaBeach.validators import file_validator

UserModel = get_user_model()


class Album(models.Model):
    photo = CloudinaryField(
        'photo',
        validators=[file_validator,]
    )
    photo_type = models.CharField(
        max_length=10,
        choices=PhotoTypesChoices.choices
    )
    description = models.TextField()
    published_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    upload_date = models.DateTimeField(
        auto_now_add=True
    )
    apartment = models.ForeignKey(
        to=Apartment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price_per_night = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    price = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
        default='BGN',
    )

    def get_price_for_rent(self):
        return f'{self.price_per_night:.2f} {self.currency}'

    def get_price_for_sale(self):
        return f'{self.price} {self.currency}'

