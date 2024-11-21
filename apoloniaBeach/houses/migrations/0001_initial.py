# Generated by Django 5.1.2 on 2024-11-16 08:33

import apoloniaBeach.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1)),
                ('lift', models.BooleanField(default=False)),
                ('floors', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('common_corridors', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2, validators=[apoloniaBeach.validators.AlphaNumericValidator()])),
                ('apartment_area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('common_parts_of_the_building', models.DecimalField(decimal_places=2, max_digits=5)),
                ('for_rental', models.BooleanField(default=False)),
                ('for_sale', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='apartment_pictures')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='houses.house')),
            ],
        ),
    ]
