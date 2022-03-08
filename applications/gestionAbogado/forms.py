from django import forms

from .models import GestionAbogado

class GestionAbogadoForm(forms.ModelForm):

    class Meta:
        
        model = GestionAbogado

        fields = ('user', 'deudores', 'califiacion_viabilidad', 'observaciones',
                  'archivo', 'archivo2', 'archivo3', 'archivo4', 'archivo5',
                  'archivo6')