from django import forms
from django.contrib.auth import authenticate

from .models import CastigoCartera
from applications.users.models import User



class CastigadosForm(forms.ModelForm):
    users = []
    usuarios = User.objects.abogadosUsers()
    for i in usuarios:
        x = (i.pk, i.full_name)
        users.append(x)

    users = forms.MultipleChoiceField(choices=users)
    
    class Meta:
        model = CastigoCartera
        fields = ('archivo', 'archivo2', 'archivo3', 'archivo4', 'archivo5',
                  'archivo6', 'calificacion_viabilidad', 'observaciones', 'deudor', 'usuario')
        widgets = {
            'observaciones' : forms.Textarea(
                attrs = {
                    'placeholder' : 'Lo que quieras poner'
                }
            )
        }