# Generated by Django 4.2.6 on 2023-11-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_remove_endcustomer_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endcustomer',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Télefono de contacto'),
        ),
    ]
