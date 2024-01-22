from django.db import models

from bi360.business.models import Business


# Create your models here.
class Employee(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True, verbose_name="Código colaborador")
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos", blank=True)
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    salary = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Remuneración")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_date = models.DateField()
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)
    earnings = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Nómina para {self.employee} en {self.pay_date}"
