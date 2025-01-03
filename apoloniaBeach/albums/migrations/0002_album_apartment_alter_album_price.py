# Generated by Django 5.1.2 on 2024-11-19 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.apartment'),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
