from django import forms
from django.contrib.auth import authenticate

from .models import User
from applications.deudor.models import Deudor

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'position',
            'genero',
            'date_birth',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')




class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'username',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data




class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    email_pass = forms.CharField(
        label = 'Contraseña del correo',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña de tu correo'
            }
        )
    )


class ForgotPswd(forms.ModelForm):


    class Meta:
        model = User
        fields = {
            'first_time','password'
        }
        widgets = {
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Nueva Contraseña',
                    'class': 'input-group-field',
                }
            )
        }
        


class AgendarForm(forms.ModelForm):

    class Meta:
        model = Deudor
        fields = {
            'fecha_nueva_accion',
        }
        widgets = {
            'fecha_nueva_accion': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                }
            )
        }