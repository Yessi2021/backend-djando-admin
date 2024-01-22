from django.db import models

from bi360.business.models import Business


# Create your models here.
class Seller(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    identification = models.CharField(max_length=100, unique=True, verbose_name="Identificación")
    names = models.CharField(max_length=150, verbose_name="Nombres")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    birthday = models.DateField(null=True, verbose_name="Fecha")
    address = models.TextField(blank=True, null=True, verbose_name="Dirección")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Télefono de contacto")

    def __str__(self):
        return self.names
