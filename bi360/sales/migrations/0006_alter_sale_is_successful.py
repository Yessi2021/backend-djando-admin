# Generated by Django 4.2.6 on 2023-11-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_sale_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='is_successful',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
