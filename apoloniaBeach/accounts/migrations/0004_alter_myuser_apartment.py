# Generated by Django 5.1.2 on 2024-11-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_myuser_phone_number'),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='apartment',
            field=models.ManyToManyField(blank=True, related_name='owner', to='houses.apartment'),
        ),
    ]