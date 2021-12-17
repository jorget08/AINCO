from django import forms
from django.forms import fields

from applications.deudor.models import Deudor

class CastigadaForm(forms.ModelForm):
    
    class Meta:
        model = Deudor
        fields = ('castigado', 'edad')
