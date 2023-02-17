from django import forms

from .models import GestionAbogado

class GestionAbogadoForm(forms.ModelForm):

    class Meta:
        
        model = GestionAbogado

        fields = ('user', 'deudores','actuaciones_proceso','fecha_inicia_termino',
                  'fecha_finaliza_termino','fecha_registro','fecha_control',
                  'calificacion_viabilidad','observaciones','archivo',)

        widgets = {
            'fecha_control' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'fecha_registro' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'fecha_inicia_termino' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'fecha_finaliza_termino' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }