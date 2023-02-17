from django import forms
from django.forms import fields

from applications.acuerdo.models import AcuerdosPago

class AcuerdoForm(forms.ModelForm):

    class Meta:
        model = AcuerdosPago
        fields = (
            'valor_compromiso', 'forma_pago', 'evidencia',
            'fecha_1', 
            'fecha_2', 'fecha_3', 
            'valor_compromiso_2', 'valor_compromiso_3',
             'user', 'deudores',
        )
        widgets = {
            'fecha_1': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'fecha_2': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'fecha_3': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }


class AcuedoActualizacion(forms.ModelForm):
    class Meta:
        model = AcuerdosPago
        fields = ('estado_del_acuerdo', )