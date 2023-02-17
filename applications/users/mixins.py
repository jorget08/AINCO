from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
#
from .models import User


def check_ocupation_user(ocupation, user_ocupation):
    #
    
    if (ocupation == User.SuperAdminPermisoMixin or ocupation == user_ocupation):
        
        return True
    else:
        return False


class OperarioPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #comportamiento añadido 
        if not check_ocupation_user(request.user.ocupation, User.OPERARIO): # el User.tal es del modelo, las opciones de la ocupacion
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users:login'
                )
            )

        return super().dispatch(request, *args, **kwargs)


class AdminLocalPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #comportamiento añadido 
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR_LOCAL): # el User.tal es del modelo, las opciones de la ocupacion
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)


class AdminRegionalPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #comportamiento añadido 
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR_REGIONAL): # el User.tal es del modelo, las opciones de la ocupacion
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)


class SuperAdminPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #comportamiento añadido 
        if not check_ocupation_user(request.user.ocupation, User.SUPER_ADMINISTRADOR): # el User.tal es del modelo, las opciones de la ocupacion
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)