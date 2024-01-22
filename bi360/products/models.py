from django.db import models

from bi360.business.models import Business


# Create your models here.
class Product(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100, unique=True, verbose_name="Código del producto")
    product_name = models.TextField(verbose_name="Nombre del producto")
    gruop_inventory = models.TextField(verbose_name="Grupo de inventario", null=True)
    type_inventory = models.TextField(verbose_name="Tipo de inventario", null=True)
    line = models.TextField(verbose_name="Linea", null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
