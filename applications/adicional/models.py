from django.db import models

from applications.deudor.models import Deudor
from applications.conyugue.models import Conyugue
from applications.codeudor.models import Codeudor
from applications.users.models import User

# Create your models here.
class Adicionado(models.Model):
    tel_fijo_add = models.CharField(max_length=15, null = True, blank = True)
    celular_add = models.CharField(max_length=15, null = True, blank = True)
    correo_add = models.EmailField(max_length=254, null=True, blank = True)
    tel_empresa_add = models.CharField(max_length=12, null = True, blank = True)
    celular_empresa_add = models.CharField(max_length=15, null = True, blank = True)
    
    #Relaciones
    deudores = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True, blank = True, related_name = 'adicionado_deudor')
    conyugue = models.ForeignKey(Conyugue, on_delete=models.CASCADE, null = True, blank = True)
    codeudor = models.ForeignKey(Codeudor, on_delete=models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)