from django.db import models

from applications.deudor.models import Deudor
from applications.users.models import User
#from applications.acuerdo.models import AcuerdosPago

# Create your models here.

class Gestion(models.Model):

    #Constantes persona contactada
    DEUDOR = '0'
    CODEUDOR = '1'
    FAMILIAR = '2'
    REFERENCIA = '3'

    #Constantes tipo de gestion
    LLAMADA_CELULAR = '0'
    LLAMADA_FIJO = '1'
    MENSDAJE_TEXTO = '2'
    MENSAJE_WPP = '3'
    EMAIL = '4'
    VISITA_CASA = '5'
    VISITA_EMPRESA = '6'

    #Constantes resultado de la gestion
    ACUERDO_PAGO = '0'
    VISITA_OFICINA = '1'
    VOLVER_LLAMAR = '2'
    REESTRUCTURACION = '3'
    FECHA_PAGO = '4'
    CUMPLIMEINTO_ACUERDO = '5'
    NO_CUMPLIMIENTO_ACUERDO = '6'
    VISITA_CASA = '7'
    VISITA_EMPRESA = '8'

    #Constances causales de no pago
    DESEMPLEO = '0'
    DISMINUCION_INGRESOS = '1'
    PROBLEMAS_FAMILIARES = '2'
    INCAPACIDAD = '3'
    OTROS = '4'

    #Constantes calificacion de viabilidad
    VIABLE = '0'
    NO_VIABLE = '1'

    #Constantes nueva accion
    LLAMAR_FIJO = '0'
    LLAMAR_CELULAR = '1'
    MENSAJE_TEXTO = '2'
    MENSAJE_WPP = '3'
    EMAIL = '4'
    VISITA_CASA = '5'
    VISITA_EMPRESA = '6'
    ATENCION_OFICINA = '7'
    SEGUIMIENTO_ACUERDO = '8'

    #Constantes acuerdo de pago
    CUMPLIDO = '0'
    INCUMPLIDO = '1'


    PERSONA_CONTACTADA_CHOICES = [
        (DEUDOR, 'Deudor'),
        (CODEUDOR, 'Codeudor'),
        (FAMILIAR, 'Familiar'),
        (REFERENCIA, 'Referencia'),
    ]

    TIPO_GESTION_CHOICES = [
        (LLAMADA_CELULAR, 'Llamada a celular'),
        (LLAMADA_CELULAR, 'Llamada a celular'),
        (MENSDAJE_TEXTO, 'Mensaje de texto'),
        (MENSAJE_WPP, 'Mensaje de whatsapp'),
        (EMAIL, 'Envio de correo electronico'),
        (VISITA_CASA, 'Visita al domicilio'),
        (VISITA_EMPRESA, 'Visita a la empresa'),
    ]
    
    RESULTADO_GESTION_CHOICES = [
        (ACUERDO_PAGO, 'Establece acuerdo de pago'),
        (VISITA_OFICINA, 'Visitará la oficina'),
        (VOLVER_LLAMAR, 'Volver a llamar'),
        (FECHA_PAGO, 'Solicita cambio de fecha de pago'),
        (CUMPLIMEINTO_ACUERDO, 'Cumplio con el acuerdo de pago'),
        (NO_CUMPLIMIENTO_ACUERDO, 'No cumplio con el acuerdo de pago'),
        (VISITA_CASA, 'Visita al domicilio'),
        (VISITA_EMPRESA, 'Visita a la empresa'),
    ]
    
    CAUSALES_NO_PAGO_CHOICES = [
        (DESEMPLEO, 'Desempleo'),
        (DISMINUCION_INGRESOS, 'Disminición de ingresos'),
        (PROBLEMAS_FAMILIARES, 'Problemas familiares'),
        (INCAPACIDAD, 'Se encuentra incapacitado'),
        (OTROS, 'Otros'),
    ]
    
    CALIFIACION_VIABILIDAD_CHOICES = [
        (VIABLE, 'Viable'),
        (NO_VIABLE, 'No viable'),
    ]

    NUEVA_ACCION_CHOICES = [
        (LLAMAR_FIJO, 'Llamar al fijo'),
        (LLAMAR_CELULAR, 'Llamar al celular'),
        (MENSAJE_TEXTO, 'Enviar mensaje de texto'),
        (MENSAJE_WPP, 'Enviar mensaje por whatsapp'),
        (EMAIL, 'Enviar correo electrónico'),
        (VISITA_CASA, 'Visitar al domicilio'),
        (VISITA_EMPRESA, 'Visitar en la empresa'),
        (ATENCION_OFICINA, 'Atención en la oficina'),
        (SEGUIMIENTO_ACUERDO, 'Seguimiento al acuerdo de pago'),
    ]
    
    #ESTADO_ACUERDO_PAGO_CHOICES = [
    #    (CUMPLIDO, 'Cumplido'),
    #    (INCUMPLIDO, 'No cumplido')
    #]

    persona_contactada = models.CharField(max_length=2, choices=PERSONA_CONTACTADA_CHOICES)
    fecha_gestion = models.DateField(auto_now_add=True)
    nombre_parentesco = models.CharField(max_length=100)
    tipo_gestion = models.CharField(max_length=2, choices=TIPO_GESTION_CHOICES)
    resultado_gestion = models.CharField(max_length=200, choices=RESULTADO_GESTION_CHOICES)
    observaciones = models.TextField()
    comentarios = models.TextField(blank=True)
    causales_no_pago = models.CharField(max_length=2, choices=CAUSALES_NO_PAGO_CHOICES)
    califiacion_viabilidad = models.CharField(max_length=2, choices=CALIFIACION_VIABILIDAD_CHOICES)
    fecha_nueva_accion = models.DateField()
    nueva_accion = models.CharField(max_length=2, choices=NUEVA_ACCION_CHOICES)
    hora_nueva_accion = models.TimeField()
    
    #estado_acuerdo_pago = models.CharField(max_length=2, choices=ESTADO_ACUERDO_PAGO_CHOICES, blank = True, null = True)

    #castigada = models.BooleanField(default=False)
    evidencia = models.FileField(upload_to='acuerdos', blank = True)
    
    modified = models.DateTimeField(auto_now=True)

    # Relaciones
    deudores = models.ForeignKey(Deudor, on_delete=models.CASCADE, null = True, related_name="gestion_deudor")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    #acuerdo_pago = models.ForeignKey(AcuerdosPago, on_delete=models.CASCADE, null = True, blank = True)


    def __str__(self):
        x = self.PERSONA_CONTACTADA_CHOICES[int(self.persona_contactada)]
        return x[1]

    def get_persona_contactada(self):
        x = self.PERSONA_CONTACTADA_CHOICES[int(self.persona_contactada)]
        return x[1]
    
    def get_tipo_gestion(self):
        x = self.TIPO_GESTION_CHOICES[int(self.tipo_gestion)]
        return x[1]

    def get_resultado_gestion(self):
        x = self.RESULTADO_GESTION_CHOICES[int(self.resultado_gestion)]
        return x[1]

    def get_causales_no_pago(self):
        x = self.CAUSALES_NO_PAGO_CHOICES[int(self.causales_no_pago)]
        return x[1]

    def get_califiacion_viabilidad(self):
        x = self.CALIFIACION_VIABILIDAD_CHOICES[int(self.califiacion_viabilidad)]
        return x[1]

    def get_nueva_accion(self):
        x = self.NUEVA_ACCION_CHOICES[int(self.nueva_accion)]
        return x[1]

    def get_estado_acuerdo_pago(self):
        x = self.ESTADO_ACUERDO_PAGO_CHOICES[int(self.nueva_accion)]
        return x[1]


    def __str__(self):
        return self.deudores.nombres

    def save(self, *args, **kwargs):
        self.deudores.fecha_nueva_accion = self.fecha_nueva_accion
        self.deudores.hora_nueva_accion = self.hora_nueva_accion
        self.deudores.nueva_accion = self.get_nueva_accion()
        self.deudores.comentarios = self.comentarios
        self.deudores.contador_gestiones = self.deudores.contador_gestiones + 1
        self.deudores.save()

        super(Gestion, self).save(*args, **kwargs)
