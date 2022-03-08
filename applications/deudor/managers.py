import numpy as np

from datetime import date

from django.db import models
from django.db.models import Sum
from django.db.models import Q

class DeudorManager(models.Manager):
    
    
    def totales(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False).filter(
            fecha_nueva_accion=None
            ).order_by('-total_insolutos')
        return deudores

    
    def listado(self, usuario, kword):
        deudores = self.filter(usuarios=usuario).filter(castigado=False)
        consulta = deudores.order_by('fecha_nueva_accion', '-total_insolutos').exclude(fecha_nueva_accion=None).filter(
            Q(nombres__icontains=kword) | Q(apellidos__icontains=kword) | Q(full_name__icontains=kword)
        )
        return consulta

    
    def listadoAbogado(self, usuario, kword):
        deudores = self.filter(usuarios=usuario)
        consulta = deudores.order_by('fecha_nueva_accion', '-total_insolutos').exclude(fecha_nueva_accion=None).filter(
            Q(nombres__icontains=kword) | Q(apellidos__icontains=kword) | Q(full_name__icontains=kword)
        )
        return consulta

    
    def dedudores_dia(self,usuario):
        today = date.today()
        return self.filter(usuarios=usuario).filter(fecha_nueva_accion = today).filter(castigado=False).count()


    def creditos_mes(self,usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False)
        l = []
        for i in deudores:
            x = i.credito_deudor.count()
            l.append(x)
        
        np_list = np.array(l)
                
        return np_list.sum()


    def creditos_dia(self,usuario):
        today = date.today()
        deudores = self.filter(usuarios=usuario).filter(castigado=False).filter(fecha_nueva_accion = today)
        l = []
        for i in deudores:
            x = i.credito_deudor.count()
            l.append(x)
        
        np_list = np.array(l)
                
        return np_list.sum()
    
    
    def sal_in_mes(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False)
        l = []
        for i in deudores:
            x = i.credito_deudor.aggregate(sld_ins = Sum('saldo_insoluto'))
            l.append(x['sld_ins'])
        
        np_list = np.array(l)
                
        return np_list.sum()


    
    def sal_in_dia(self,usuario):
        today = date.today()
        deudores = self.filter(usuarios=usuario).filter(castigado=False).filter(fecha_nueva_accion = today)
        l = []
        for i in deudores:
            x = i.credito_deudor.aggregate(sld_ins = Sum('saldo_insoluto'))
            l.append(x['sld_ins'])
        
        np_list = np.array(l)
                
        return np_list.sum()



    def gestionados(self, usuario):
        return self.filter(usuarios=usuario).filter(castigado=False).exclude(contador_gestiones = 0).count()



    def gestionados_creditos(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False).exclude(contador_gestiones = 0)
        l = []
        for i in deudores:
            x = i.credito_deudor.count()
            l.append(x)
        
        np_list = np.array(l)
                
        return np_list.sum()


    def porcentaje_gestionados(self, usuario):
        deudores_mes = self.filter(usuarios=usuario).filter(castigado=False).count()
        deudores_gestionados = self.filter(usuarios=usuario).filter(
            castigado=False
            ).exclude(contador_gestiones = 0).count()
        if deudores_mes == 0:
            return 0
        else:
            return round((deudores_gestionados*100)/deudores_mes, 2)


    def porcentaje_gestionados_creditos(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False)
        l = []
        for i in deudores:
            x = i.credito_deudor.count()
            l.append(x)
        
        np_list = np.array(l)
                
        creditos_mes = np_list.sum()

        deudors = self.filter(usuarios=usuario).filter(castigado=False).exclude(contador_gestiones = 0)
        le = []
        for i in deudors:
            x = i.credito_deudor.count()
            le.append(x)
        
        np_lista = np.array(le)
                
        gestionados = np_lista.sum()

        return round((gestionados*100)/creditos_mes, 2)

        
    def context_deudor(self, kword):
        if self.filter(pk=kword).exists() == True:
            return self.get(pk=kword)

        else:
            return None
    


    def nomalizados(self, usuario):
        return self.filter(usuarios=usuario).filter(castigado=False).filter(credito_deudor__normalizado=True).count()


    def nomalizados_saldo(self, usuario):
        x = self.filter(usuarios=usuario).filter(castigado=False).filter(
            credito_deudor__normalizado=True
            ).aggregate(sld_ins = Sum('credito_deudor__saldo_insoluto'))
        return x['sld_ins']
        

    def nomalizados_vencidos(self, usuario):
        return self.filter(usuarios=usuario).filter(castigado=False).filter(
            Q(credito_deudor__vencido=True), Q(credito_deudor__dias_mora=0)
            ).count()


    def normalizados_vencidos_saldo(self, usuario):
        x = self.filter(usuarios=usuario).filter(castigado=False).filter(
            Q(credito_deudor__vencido=True), Q(credito_deudor__dias_mora=0)
            ).aggregate(sld_ins = Sum('credito_deudor__saldo_insoluto'))
        return x['sld_ins']


    def porcentaje_normalizados(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=False)
        l = []
        for i in deudores:
            x = i.credito_deudor.count()
            l.append(x)
        
        np_list = np.array(l)
                
        creditos_mes = np_list.sum()

        creditos_normalizados = self.filter(usuarios=usuario).filter(
            castigado=False
            ).filter(credito_deudor__vencido=False).count()

        return round((creditos_normalizados*100)/creditos_mes, 2)


    def porcentaje_normalizados_vencidos(self, usuario):
        vencidos = usuario.contador_creditos_vencidos
        normalizados_vencidos = self.filter(usuarios=usuario).filter(castigado=False).filter(
            Q(credito_deudor__vencido=True), Q(credito_deudor__dias_mora=0)
            ).count()
        if vencidos == 0:
            return 0
        else:
            return round((normalizados_vencidos*100)/vencidos, 2)


    def castigados(self, usuario):
        deudores = self.filter(usuarios=usuario).filter(castigado=True)
        return deudores


    def total_insoluto_vencidos(self, usuario):
        x = self.filter(usuarios=usuario).filter(castigado=False).filter(
            credito_deudor__vencido=True).aggregate(sld_ins = Sum('credito_deudor__saldo_insoluto'))
        return x['sld_ins']
