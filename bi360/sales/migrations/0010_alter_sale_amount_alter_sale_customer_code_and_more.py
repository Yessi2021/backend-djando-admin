# Generated by Django 4.2.6 on 2023-11-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_alter_sale_customer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor unitario'
            ),
        ),
        migrations.AlterField(
            model_name='sale',
            name='customer_code',
            field=models.CharField(max_length=50, null=True, verbose_name='Código del cliente'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='final_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Valor total'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='is_successful',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product_code',
            field=models.CharField(max_length=50, null=True, verbose_name='Código del producto'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product_quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(null=True, verbose_name='Fecha de la venta'),
        ),
    ]