from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # TIPO DE USUARIOS
    OPERARIO = '0'
    ADMINISTRADOR_LOCAL = '1'
    ADMINISTRADOR_REGIONAL = '2'
    SUPER_ADMINISTRADOR = '3'
    # GENEROS
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #
    OCUPATION_CHOICES = [
        (OPERARIO, 'Operario'),
        (ADMINISTRADOR_LOCAL, 'Administrador de local'),
        (ADMINISTRADOR_REGIONAL, 'Administrador de region'),
        (SUPER_ADMINISTRADOR, 'Super administrador')
    ]

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otro'),
    ]

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    position = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_time = models.BooleanField(default=False)

    #contador
    contador_creditos_vencidos = models.IntegerField(default=0)
    total_insoluto_mes = models.BigIntegerField(default=0)

    pass_email = models.CharField('Password de email', max_length=120, blank=True, null=True)#Quitar el blank y null

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email'] 
    
    objects = UserManager()

    def get_full_name(self):
        return str(self.full_name)

    def __str__(self):
        return self.full_name
