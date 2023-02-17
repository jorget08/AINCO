from django.db import models

# Create your models here.

class Bilbio(models.Model):
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_vigencia = models.DateField()
    tema = models.CharField(max_length=200)
    documento = models.FileField(upload_to='biblioteca', blank = True)

    def __str__(self):
        return self.tema