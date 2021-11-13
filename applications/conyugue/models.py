from django.db import models

from applications.deudor.models import Deudor
from .managers import ConygueManager
# Create your models here.
class Conyugue(models.Model):
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    correo = models.EmailField(max_length=254)
    empresa_labora = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    cargo = models.CharField(max_length=70)
    fijo = models.CharField(max_length=7, blank = True)

    objects = ConygueManager()
    
    #Relaciones
    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True)