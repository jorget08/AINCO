from django.db import models

from applications.deudor.models import Deudor

# Create your models here.

class CastigoCartera(models.Model):

    #Constantes calificacion de viabilidad
    VIABLE = '0'
    NO_VIABLE = '1'

    CALIFIACION_VIABILIDAD_CHOICES = [
        (VIABLE, 'Viable'),
        (NO_VIABLE, 'No viable'),
    ]

    fecha_asignacion = models.DateField(auto_now_add=True)
    archivo = models.FileField(upload_to='documentosDeudores', blank = True)
    archivo2 = models.FileField(upload_to='documentosDeudores', blank = True)
    archivo3 = models.FileField(upload_to='documentosDeudores', blank = True)
    archivo4 = models.FileField(upload_to='documentosDeudores', blank = True)
    archivo5 = models.FileField(upload_to='documentosDeudores', blank = True)
    archivo6 = models.FileField(upload_to='documentosDeudores', blank = True)
    calificacion_viabilidad = models.CharField(max_length=2, choices=CALIFIACION_VIABILIDAD_CHOICES)
    observaciones = models.TextField(blank = True)
    usuario = models.CharField(max_length=15, blank=True)

    #relaciones
    deudor = models.OneToOneField(Deudor, on_delete=models.CASCADE, related_name="castigo_deudor")

    def get_califiacion_viabilidad(self):
        x = self.CALIFIACION_VIABILIDAD_CHOICES[int(self.califiacion_viabilidad)]
        return x[1]
