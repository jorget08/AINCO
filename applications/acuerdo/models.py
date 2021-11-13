from django.db import models

from applications.users.models import User
from applications.deudor.models import Deudor

# Create your models here.

class AcuerdosPago(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    valor_compromiso = models.BigIntegerField()
    forma_pago = models.CharField(max_length=50)
    evidencia = models.FileField(upload_to='acuerdos', blank = True)
    fecha_1 = models.DateField(null = True)
    fecha_2 = models.DateField(blank=True, null = True)
    fecha_3 = models.DateField(blank=True, null = True)
    valor_compromiso_2 = models.BigIntegerField(blank=True, null = True)
    valor_compromiso_3 = models.BigIntegerField(blank=True, null = True)


    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    deudores = models.OneToOneField(Deudor, on_delete=models.CASCADE, null = True, related_name="acuerdo_deudor")
