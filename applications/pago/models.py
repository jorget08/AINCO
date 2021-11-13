from django.db import models

from applications.deudor.models import Deudor

# Create your models here.

class Pagos(models.Model):
    #MODELO
    fecha_pago = models.DateField()
    tipo_pago_aplicado = models.CharField(max_length=200)
    forma_pago = models.CharField(max_length=200)
    valor_pago = models.BigIntegerField()
    no_recibo_pago = models.IntegerField()
    valor_abono_saldo_credito = models.BigIntegerField()
    valor_abono_intereses_corrientes = models.IntegerField()
    valor_abono_intereses_moratorios = models.IntegerField()
    valor_gastos_cobranza = models.IntegerField()
    valor_abono_honorarios = models.IntegerField()
    
    #Relaciones
    deudores = models.ForeignKey(Deudor, on_delete=models.CASCADE)