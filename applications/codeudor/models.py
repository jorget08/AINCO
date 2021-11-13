from django.db import models

from applications.deudor.models import Deudor
from .managers import CodeudorManager
# Create your models here.
class Codeudor(models.Model):
    #MODELO
    codigo_codeudor = models.BigIntegerField(unique=True)
    cedula = models.BigIntegerField(primary_key=True, unique=True,)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    estado = models.CharField(max_length=20)
    fecha_exp_cedula = models.DateField()
    ocupacion = models.CharField(max_length=60)
    profesion = models.CharField(max_length=60)
    nivel_estudios = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    ciudad =models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    tel_fijo = models.PositiveIntegerField(default=0, blank = True, null = True)
    celular = models.CharField(max_length=10)
    tel_fijo2 = models.PositiveIntegerField(default=0, blank = True, null = True)
    celular2 = models.CharField(max_length=10, blank = True, null = True)
    eps = models.CharField(max_length=60)

    objects = CodeudorManager()
    
    #RELACIONES
    deudores = models.ManyToManyField(Deudor)
    #usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    #administradores = models.ForeignKey(Admin, on_delete=models.CASCADE)
    #conyugues = models.ForeignKey(Conyugue, on_delete=models.CASCADE)
    #empresas = models.OneToOneField(Empresa, on_delete=models.CASCADE)
    #sedes = models.ManyToManyField(Sede)
    #referencias = models.ManyToManyField(Referencias)

    def __str__(self):
        return self.nombres