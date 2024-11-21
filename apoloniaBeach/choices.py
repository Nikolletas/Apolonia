from django.db import models


class HouseChoices(models.TextChoices):
    A = 'A', 'A',
    B = 'B', 'B',
    C = 'C', 'C',
    D = 'D', 'D',
    E = 'E', 'E',
    F = 'F', 'F',


class DocumentChoices(models.TextChoices):
    RULES = 'Rules', 'Rules',
    PROTOCOL = 'Protocol', 'Protocol',
    LETTERS = 'Letters', 'Letters',
    OFFERS = 'Offers', 'Offers',
    INVITATION = 'Invitation', 'Invitation',
    REPORTS = 'Reports', 'Reports'
    OTHER = 'Other', 'Other',


class PhotoTypesChoices(models.TextChoices):
    COMMON = 'Common', 'Common',
    RENTAL = 'Rental', 'Rental',
    SALE = 'Sale', 'Sale',


class CurrencyChoices(models.TextChoices):
    USD = 'USD', 'USD',
    EUR = 'EUR', 'EUR',
    BGN = 'BGN', 'BGN',
