from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apoloniaBeach.houses.models import Apartment
from .managers import UserRegistrationManager
from apoloniaBeach.validators import NameLetterValidator, NumericValidator


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'required': "This field is required!",
            'invalid': "Please enter a valid email address!"
        }
    )
    first_name = models.CharField(
        max_length=40,
        validators=[NameLetterValidator(), ],
    )
    last_name = models.CharField(
        max_length=40,
        validators=[NameLetterValidator(), ]
    )
    nationality = models.CharField(
        max_length=40,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[NumericValidator(), ]
    )
    apartment = models.ManyToManyField(
        to=Apartment,
        blank=True,
        related_name='owner'
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserRegistrationManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
    )


