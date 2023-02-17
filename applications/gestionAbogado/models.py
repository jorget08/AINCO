from django.db import models

from applications.deudor.models import Deudor
from applications.users.models import User

# Create your models here.

class GestionAbogado(models.Model):

    #Constantes calificacion de viabilidad
    VIABLE = '0'
    NO_VIABLE = '1'

    CALIFIACION_VIABILIDAD_CHOICES = [
        (VIABLE, 'Viable'),
        (NO_VIABLE, 'No viable'),
    ]

    fecha_gestionAbogado = models.DateTimeField(auto_now_add=True, blank=True)
    actuaciones_proceso = models.CharField(max_length=200, blank=True)
    fecha_inicia_termino = models.DateField(blank=True, null=True)
    fecha_finaliza_termino = models.DateField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_control = models.DateField(blank=True, null=True)
    calificacion_viabilidad = models.CharField(max_length=2, choices=CALIFIACION_VIABILIDAD_CHOICES, blank=True)
    observaciones = models.TextField(blank=True)
    archivo = models.FileField(upload_to='gestionAbogado', blank = True)

    # Relaciones
    deudores = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True, related_name="gestionAbogado_deudor")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def get_calificacion_viabilidad(self):
        x = self.CALIFIACION_VIABILIDAD_CHOICES[int(self.calificacion_viabilidad)]
        return x[1]


    def save(self, *args, **kwargs):
        self.deudores.fecha_nueva_accion = self.fecha_control
        self.deudores.save()
        super(GestionAbogado, self).save(*args, **kwargs)
