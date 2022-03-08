from django.db import models

from applications.users.models import User
from .managers import DeudorManager

# Create your models here.
class Deudor(models.Model):
    #MODELO
    cedula = models.BigIntegerField(primary_key=True, unique=True)
    codigo_deudor = models.BigIntegerField(unique=True)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    estado = models.CharField(max_length=20)
    fecha_exp_cedula = models.DateField()
    ocupacion = models.CharField(max_length=60)
    profesion = models.CharField(max_length=60)
    nivel_estudios = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    ingresos_reportados = models.BigIntegerField()
    personas_a_cargo = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    ciudad =models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    tel_fijo = models.CharField(max_length=15, blank = True, null = True)
    celular = models.CharField(max_length=15)
    tel_fijo2 = models.CharField(max_length=15, blank = True, null = True)
    celular2 = models.CharField(max_length=15, blank = True, null = True)
    eps = models.CharField(max_length=60)
    aportes_sociales_vencidos = models.IntegerField(default=0)

    #Nuevas variables
    total_insolutos = models.BigIntegerField(default=0)
    total_provisiones = models.BigIntegerField(default=0)
    total_estar_al_dia = models.BigIntegerField(default=0)
    total_credito = models.BigIntegerField(default=0)
    total_liberar_provision = models.BigIntegerField(default=0)
    
    fecha_nueva_accion = models.DateField(blank=True, null = True)
    hora_nueva_accion = models.TimeField(blank=True, null = True)
    nueva_accion = models.CharField(max_length=200, blank=True, null = True)
    comentarios = models.TextField(blank=True, null = True)
    contador_gestiones = models.IntegerField(default=0)

    dia_max_corte = models.SmallIntegerField(default=0)
    dia_max_mora = models.PositiveSmallIntegerField(default=0)
    estado_inicial = models.CharField(max_length=20, blank=True, null=True)

    castigado = models.BooleanField(default=False)

    full_name = models.CharField(max_length=120, blank = True, null = True)
    
    objects = DeudorManager()
    
    #RELACIONES
    usuarios = models.ManyToManyField(User, blank=True, related_name='deudor_usuarios')
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    """administradores = models.ForeignKey(Admin, on_delete=models.CASCADE)
    sedes = models.ForeignKey(Sede, on_delete=models.CASCADE)
    calificaciones_mensuales = models.ForeignKey(CalificacionMensual, on_delete=models.CASCADE)
    referencias = models.ManyToManyField(Referencias)"""
    
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

    def get_estado_inicial(self):
        if self.dia_max_mora > 0:
            return self.estado_inicial == 'Vencido'
        else:
            return self.estado_inicial == 'Normalizado'
        


    def save(self, *args, **kwargs):
        self.full_name = self.nombres + ' ' + self.apellidos
        if self.dia_max_mora > 0:
            self.estado_inicial = 'Vencido'
        else:
            self.estado_inicial = 'Normalizado'
        super(Deudor, self).save(*args, **kwargs)