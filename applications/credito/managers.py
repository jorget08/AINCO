from django.db import models
from django.db.models import Sum
from applications.deudor.models import Deudor

class CreditoManager(models.Manager):

    def saldo_insoluto(self, deudor):
        lista = []
        for i in deudor:
            f = i.credito_deudor__saldo_insoluto
            lista.append(f)
        return lista

    def num_creditos_vencidos(self, usuario):
        return self.filter(vencido=True).filter(deudor__usuarios=usuario
        ).filter(deudor__castigado=False).count()