# Generated by Django 4.2.6 on 2023-11-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_alter_sale_amount_alter_sale_customer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Valor unitario'
            ),
        ),
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='final_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, verbose_name='Valor total'),
        ),
    ]