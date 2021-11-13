from django.db import models

from applications.deudor.models import Deudor

# Create your models here.
class Empresa(models.Model):
    #MODELO
    nombre = models.CharField(max_length=70)
    cargo_empleado = models.CharField(max_length=70)
    fecha_ingreso_laboral = models.DateField()
    tipo_contrato = models.CharField(max_length=70)
    direccion = models.CharField(max_length=70)
    barrio = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=70)
    departamento = models.CharField(max_length=70)
    correo_laboral = models.EmailField(max_length=254)
    tel_fijo = models.CharField(max_length=7, blank = True)
    celular = models.CharField(max_length=10)
    
    #Relaciones
    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True, related_name = 'empresa_deudor')
    
    def __str__(self):
        return self.nombre