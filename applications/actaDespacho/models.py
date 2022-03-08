from django.db import models

from applications.deudor.models import Deudor
from applications.users.models import User

# Create your models here.

class ActaDespacho(models.Model):

    fecha_subida_acto = models.DateTimeField(auto_now_add=True)
    fecha_acta = models.DateField()
    num_radicacion = models.CharField(max_length=200)
    clase_proceso = models.CharField(max_length=250)
    num_despacho = models.CharField(max_length=200)
    nombre_despacho = models.CharField(max_length=200)
    juez_o_magistrado = models.CharField(max_length=250)
    direccions_despacho = models.CharField(max_length=250)
    ciudad_despacho = models.CharField(max_length=150)
    tel_fijo = models.CharField(max_length=7, blank=True)
    tel_fijo2 = models.CharField(max_length=7, blank=True)
    cel = models.CharField(max_length=10, blank=True)
    cel2 = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    email2 = models.EmailField(max_length=250, blank=True)
    observaciones = models.TextField(blank=True)
    comentarios = models.TextField(blank=True)
    acta = models.FileField(upload_to='gestionActas')

    #relaciones
    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE, related_name='actaDespacho_deudor')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actaDespacho_user')
