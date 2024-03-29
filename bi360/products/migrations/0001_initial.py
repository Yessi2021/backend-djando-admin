# Generated by Django 4.2.6 on 2023-10-23 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0002_business_license_expiration_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
    ]
