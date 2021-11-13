from django.db import models

# Create your models here.
class CalificacionMensual(models.Model):
    calificacion = models.CharField(max_length=2)
    fecha = models.DateField()