from django.db import models

from bi360.business.models import Business


# Create your models here.
class Sale(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    transaction_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Identificador de la transacción",
        null=True,
    )
    transaction_type = models.CharField(max_length=50, null=True, verbose_name="Tipo de transacción")
    channel = models.CharField(max_length=50, null=True, verbose_name="Canal de la transacción")
    product_code = models.CharField(max_length=50, null=True, verbose_name="Código del producto")
    customer_code = models.CharField(max_length=50, null=True, verbose_name="Código del cliente")
    seller_code = models.CharField(max_length=50, null=True, verbose_name="Código del vendedor")
    sale_date = models.DateField(null=True, verbose_name="Fecha")
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name="Cantidad")
    unit_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Valor unitario",
    )
    discount_value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, verbose_name="Descuento")

    def __str__(self):
        return f"Venta {self.transaction_id} de la empresa {self.business.name}"
