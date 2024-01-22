from django.db import models

from bi360.business.models import Business


# Create your models here.
class Configuration(models.Model):
    related_model = models.ForeignKey(Business, on_delete=models.CASCADE)
    # Campo para el nombre de la configuración
    name = models.CharField(max_length=100)
    # La tabla destino de la configuración
    destination_table = models.CharField(max_length=100)
    # La hoja seleccionada para la configuración
    selected_sheet = models.CharField(max_length=50)
    # El índice de los headers en la hoja de cálculo
    headers_index = models.IntegerField()
    # Un campo para almacenar una relación entre las columnas del archivo y las columnas de la tabla seleccionada.
    # Esto se puede implementar como un campo de texto que contenga una representación JSON de la relación.
    columns_mapping = models.JSONField()

    def __str__(self):
        return self.name
