# Generated by Django 4.2.6 on 2023-10-23 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_business_license_expiration_date_and_more'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_number', models.CharField(max_length=50, unique=True)),
                ('issue_date', models.DateField()),
                ('customer_code', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reason', models.TextField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
    ]
