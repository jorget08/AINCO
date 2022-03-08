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

    fecha_gestionAbogado = models.DateTimeField(auto_now_add=True)
    califiacion_viabilidad = models.CharField(max_length=2, choices=CALIFIACION_VIABILIDAD_CHOICES)
    observaciones = models.TextField(blank=True)
    archivo = models.FileField(upload_to='gestionAbogado', blank = True)
    archivo2 = models.FileField(upload_to='gestionAbogado', blank = True)
    archivo3 = models.FileField(upload_to='gestionAbogado', blank = True)
    archivo4 = models.FileField(upload_to='gestionAbogado', blank = True)
    archivo5 = models.FileField(upload_to='gestionAbogado', blank = True)
    archivo6 = models.FileField(upload_to='gestionAbogado', blank = True)

    # Relaciones
    deudores = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True, related_name="gestionAbogado_deudor")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)