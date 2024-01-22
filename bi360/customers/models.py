from django.db import models

from bi360.business.models import Business


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    phone1 = models.CharField(max_length=15, blank=True, null=True)
    business = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    message = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contacto de {self.customer.name} en {self.created_at}"


class Valuation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tools = models.IntegerField(null=True, default=None)
    standars = models.IntegerField(null=True, default=None)
    avaliability = models.IntegerField(null=True, default=None)
    level = models.IntegerField(null=True, default=None)
    management = models.IntegerField(null=True, default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    business = models.CharField(max_length=255)

    def __str__(self):
        # Calcula la suma de los valores enteros
        total = sum(
            value for value in [
                self.tools,
                self.standars,
                self.avaliability,
                self.level,
                self.management,
            ] if value is not None
        )
        return f"Valoración para {self.customer.name} (Suma: {total})"


class EndCustomer(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=50, unique=True, verbose_name="Código del cliente")
    name = models.CharField(max_length=150, verbose_name="Nombres", null=True)
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Télefono de contacto")
    address = models.TextField(blank=True, null=True, verbose_name="Dirección")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ciudad")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="País")

    def __str__(self):
        return f"{self.name}"
