# Generated by Django 5.1.2 on 2024-11-26 15:36

import apoloniaBeach.validators
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_owner_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[apoloniaBeach.validators.file_validator], verbose_name='profile_pictures'),
        ),
    ]
