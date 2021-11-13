from django import forms

from .models import Gestion
from applications.adicional.models import Adicionado
from applications.deudor.models import Deudor

class GestionForm(forms.ModelForm):
    
    
    class Meta:
        model = Gestion
        
        fields = (
            'user', 'deudores','persona_contactada', 'nombre_parentesco', 'tipo_gestion', 'resultado_gestion', 'observaciones',
            'causales_no_pago', 'califiacion_viabilidad', 'fecha_nueva_accion', 'nueva_accion','hora_nueva_accion', 'comentarios',
            'estado_acuerdo_pago', 'castigada', 'evidencia',
        )

        widgets = {
            'persona_contactada':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'tipo_gestion':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'resultado_gestion':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'causales_no_pago':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'califiacion_viabilidad':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'nueva_accion':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'estado_acuerdo_pago':forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            
        }
        


class AddInfoForm(forms.ModelForm):

    class Meta:
        model = Adicionado

        fields = {
            'tel_fijo_add', 'celular_add', 'correo_add', 'tel_empresa_add', 'celular_empresa_add',
            'deudores', 'conyugue', 'codeudor','user'
        }


class MailForm(forms.Form):

    subject = forms.CharField(max_length=200, label = 'Asunto:')
    message = forms.CharField(label = 'Mensaje:', widget = forms.Textarea,)
    de = forms.EmailField()
    pass_de = forms.PasswordInput()
    para = forms.EmailField(label = 'Para:')
    
