from django.db import models

# Create your models here.
class Referencias(models.Model):
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    celular = models.CharField(max_length=10)
    correo = models.EmailField(max_length=254)