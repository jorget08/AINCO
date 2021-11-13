from django.db import models

from applications.deudor.models import Deudor
from applications.codeudor.models import Codeudor
from .managers import CreditoManager


# Create your models here.
class Credito(models.Model):
    #MODELO
    codigo_credito = models.CharField(primary_key=True, unique=True, max_length=30)
    fecha_corte = models.DateField()                    # Fecha de actualizacion(Cambiar)
    segmento_riesgo = models.CharField(max_length=2)
    nivel_riesgo = models.CharField(max_length=2)
    analisis_contencion = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    forma_pago = models.CharField(max_length=20)
    clase_cartera = models.CharField(max_length=30)
    linea_credito = models.CharField(max_length=30)
    dias_mora = models.PositiveSmallIntegerField(default=0)
    franja_mora = models.CharField(max_length=30)
    valor_credito = models.BigIntegerField()
    plazo_total_meses = models.PositiveSmallIntegerField()
    fecha_desembolso = models.DateField()
    cuotas_vencidas = models.PositiveSmallIntegerField(default=0)
    cuotas_pagadas = models.PositiveSmallIntegerField()
    saldo_insoluto = models.BigIntegerField()
    valor_cuota = models.IntegerField()
    valor_cuota_mas_otros = models.IntegerField()
    pago_min_estar_al_dia = models.IntegerField()
    pago_total = models.BigIntegerField()
    pago_min_liberar_provision = models.IntegerField()
    valor_total_provision = models.BigIntegerField()
    dia_corte = models.SmallIntegerField()
    saldo_cuenta_ahorros = models.BigIntegerField()
    saldo_aportes_sociales = models.BigIntegerField()
    valor_disponible_cupo_rotativo = models.IntegerField()
    valor_seguros_vencidos = models.IntegerField()
    otros_vencidos = models.IntegerField()
    capital_obligaciones_vencidas = models.IntegerField()
    intereses_vencidos = models.IntegerField()
    intereses_mora = models.IntegerField()
    valores_gastos_prejuridico = models.IntegerField()
    valores_gastos_juridico = models.IntegerField()

    objects = CreditoManager()

    #Vencido
    vencido = models.BooleanField(default=False)

    #normalizados
    normalizado = models.BooleanField(default=False)
    
    #RELACIONES
    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE, blank=True, null = True, related_name="credito_deudor")
    codeudores = models.ManyToManyField(Codeudor, related_name="credito_codeudor", blank=True, null = True)
    #usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    #administradores = models.ForeignKey(Admin, on_delete=models.CASCADE)
    #sedes = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo_credito) + ' - ' + self.deudor.nombres + ' - ' + str(self.vencido)

    def save(self, *args, **kwargs):
        if self.dias_mora > 0:
            self.vencido = True
            self.normalizado = False
        

        elif self.dias_mora == 0:
            self.normalizado = True

        if self.deudor.dia_max_corte < self.dia_corte:
            self.deudor.dia_max_corte = self.dia_corte
            self.deudor.save()

        if self.deudor.dia_max_mora < self.dias_mora:
            self.deudor.dia_max_mora = self.dias_mora
            self.deudor.save()
        
        self.deudor.total_insolutos = self.deudor.total_insolutos + self.saldo_insoluto
        self.deudor.total_provisiones = self.deudor.total_provisiones + self.valor_total_provision
        self.deudor.total_estar_al_dia = self.deudor.total_estar_al_dia + self.pago_min_estar_al_dia
        self.deudor.total_credito = self.deudor.total_credito + self.pago_total
        self.deudor.total_liberar_provision = self.deudor.total_liberar_provision + self.pago_min_liberar_provision
        self.deudor.save()

        super(Credito, self).save(*args, **kwargs)