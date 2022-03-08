from django import forms

from .models import ActaDespacho

class ActaDespachoForm(forms.ModelForm):

    class Meta:

        model = ActaDespacho

        fields = ('fecha_acta', 'num_radicacion', 'clase_proceso', 'num_despacho',
                  'nombre_despacho', 'juez_o_magistrado', 'direccions_despacho',
                  'ciudad_despacho', 'tel_fijo', 'tel_fijo2', 'cel', 'cel2', 'email',
                  'email2', 'observaciones', 'comentarios', 'acta', 'deudor', 'user')

        Widgets = {
            'fecha_acta' : forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }