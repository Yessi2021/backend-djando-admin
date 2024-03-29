# Generated by Django 4.2.6 on 2023-11-16 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0003_business_nit_business_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=100, unique=True, verbose_name='Identificación')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('birthday', models.DateField(null=True, verbose_name='Fecha')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Dirección')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Télefono de contacto')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
    ]
