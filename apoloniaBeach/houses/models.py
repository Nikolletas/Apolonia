from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .choices import HouseChoices


class House(models.Model):
    name = models.CharField(
        max_length=1,
        choices=HouseChoices.choices,
    )
    lift = models.BooleanField(
        default=False,
    )
    floors = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )
    common_corridors = models.BooleanField(
        default=True,
    )


class Apartment(models.Model):
    house = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='apartments',
    )
    number = models.IntegerField()
    apartment_area = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    common_parts_of_the_building = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    for_rental = models.BooleanField(
        default=False,
    )
    for_sale = models.BooleanField(
        default=False,
    )

    def get_apartment_name(self):
        return f"{self.house.name}{self.number}"

    def get_full_area(self):
        return f'{self.apartment_area + self.common_parts_of_the_building}:.2f'
