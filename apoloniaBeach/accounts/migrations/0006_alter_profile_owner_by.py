# Generated by Django 5.1.2 on 2024-11-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_owner_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='owner_by',
            field=models.DateField(auto_now_add=True),
        ),
    ]