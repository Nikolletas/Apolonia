from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

from apoloniaBeach.houses.models import Apartment
from .managers import UserRegistrationManager
from .validators import NameLetterValidator


class UserRegistration(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
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


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        max_length=40,
        validators=[NameLetterValidator(),],
    )
    last_name = models.CharField(
        max_length=40,
        validators=[NameLetterValidator(),]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(18),],
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=20,
    )
    apartment = models.ManyToManyField(
        to=Apartment,
        blank=False,
        related_name='owner'
    )
