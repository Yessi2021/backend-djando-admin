from django.db import models
from django.utils import timezone

from bi360.authentication.models import User


class Business(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    license_type = models.CharField(max_length=50, null=True)
    license_expiration_date = models.DateField(null=True)
    license_renewed = models.BooleanField(default=False)

    def renew_license(self, renewal_details):
        # Implementa la lógica de renovación aquí.
        # Por ejemplo, actualiza la fecha de vencimiento y establece license_renewed en True.
        self.license_renewed = True
        self.license_expiration_date = timezone.now() + timezone.timedelta(days=365)  # Renovar por un año
        self.save()

        # Guarda el historial de renovaciones
        renewal = RenewalHistory(business=self, details=renewal_details)
        renewal.save()

    def is_license_expired(self):
        return self.license_expiration_date < timezone.now()

    def __str__(self):
        return self.name


class RenewalHistory(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    renewal_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"Renovación para {self.business.name} el {self.renewal_date}"


class UserBusinessRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    # Other fields

    def __str__(self):
        return f"{self.user.username} - {self.business.name}"
