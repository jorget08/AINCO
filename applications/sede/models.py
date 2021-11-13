from django.db import models

# Create your models here.
class Sede(models.Model):
    #MODELO
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    tel_fijo = models.CharField(max_length=7)
    celular = models.CharField(max_length=10)
    responsable = models.CharField(max_length=100)
    num_trabajadores = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre