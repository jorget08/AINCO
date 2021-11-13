from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from django.views import generic


from .models import User
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, ForgotPswd, AgendarForm
from applications.deudor.models import Deudor
from applications.credito.models import Credito
#from usuarios.models import Usuarios
#from gestion.models import Gestion


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    # Para que un FormView haga un porceso siempre necesita la funcion:
    def form_valid(self,form):

        # el create_user es del managers.py; la funcion recibe (username, email, password=None, **extra_fields) asi
        # que se los damos en el orden que los debe recibir y los que son campos extras le ponemos variable y de
        # que campo del form sale ese dato
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name=form.cleaned_data['full_name'],
            position=form.cleaned_data['position'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        
        return super(UserRegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users:registrar')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)
        
    def get_success_url(self):
        if self.request.user.first_time == True:
            success_url = reverse_lazy('users:change-password')
            return success_url
        else:
            success_url = reverse_lazy('users:agendar')
            return success_url
        
    

    
class LogoutView(generic.View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users:login'
            )
        )


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/dashboard.html'
    
    context_object_name = 'deudores'

    paginate_by = 7
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user
        #kword = self.request.GET.get("kword", '')

        #context['deudores'] = Deudor.objects.listado(usuario, kword)

        #reporte
        context['mes'] = Deudor.objects.filter(usuarios=usuario).count()
        context['dia'] = Deudor.objects.dedudores_dia(usuario)
        context['num_creditos'] = Deudor.objects.creditos_mes(usuario)
        context['num_creditos_dia'] = Deudor.objects.creditos_dia(usuario)
        context['sal_in_mes'] = Deudor.objects.sal_in_mes(usuario)
        context['sal_in_dia'] = Deudor.objects.sal_in_dia(usuario)
        context['gestionados'] = Deudor.objects.gestionados(usuario)
        context['gestionados_creditos'] = Deudor.objects.gestionados_creditos(usuario)
        context['porcentaje_gestionados'] = Deudor.objects.porcentaje_gestionados(usuario)
        context['normalizados'] = Deudor.objects.nomalizados(usuario)
        context['normalizados_saldos'] = Deudor.objects.nomalizados_saldo(usuario)
        context['porcentaje_gestionados_creditos'] = Deudor.objects.porcentaje_gestionados_creditos(usuario)
        context['num_vencidos'] = self.request.user.contador_creditos_vencidos
        context['insolutos_vencidos'] = self.request.user.total_insoluto_mes
        context['normalizados_vencidos'] = Deudor.objects.nomalizados_vencidos(usuario)
        context['normalizados_vencidos_saldos'] = Deudor.objects.normalizados_vencidos_saldo(usuario)
        context['porcentaje_normalizados'] = Deudor.objects.porcentaje_normalizados(usuario)
        context['porcentaje_normalizados_vencidos'] = Deudor.objects.porcentaje_normalizados_vencidos(usuario)


        #import pdb; pdb.set_trace()
        return context
    
    def get_queryset(self):

        usuario = self.request.user
        kword = self.request.GET.get("kword", '')

        resultado=Deudor.objects.listado(usuario, kword)

        return resultado



class AgendarView(LoginRequiredMixin, FormView):
    template_name = 'users/agendar.html'
    form_class = AgendarForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['deudores'] = Deudor.objects.totales(usuario)

        return context

    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=request.POST['deudores'])
        deudor.fecha_nueva_accion = request.POST['fecha_nueva_accion']
        vencidos = Deudor.objects.filter(cedula=request.POST['deudores']).filter(credito_deudor__vencido=True).count()
        insoluto_mes = Deudor.objects.filter(cedula=request.POST['deudores']).filter(credito_deudor__vencido=True).aggregate(
            sld_ins = Sum('credito_deudor__saldo_insoluto')
        )

        usuario = self.request.user
        usuario.contador_creditos_vencidos = usuario.contador_creditos_vencidos + vencidos
        usuario.total_insoluto_mes = usuario.total_insoluto_mes + insoluto_mes['sld_ins']

        usuario.save()
        deudor.save()

        return HttpResponseRedirect(reverse('users:agendar'))
        




class ChangePwd(LoginRequiredMixin, generic.FormView):
    template_name = 'users/change-pswd.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.first_time = False
            usuario.pass_email = form.cleaned_data['email_pass']
            usuario.save()

        logout(self.request)
        return super(ChangePwd, self).form_valid(form)


class UsersList(generic.ListView):
    template_name = 'users/lista-users.html'
    model = User


class RecuPswd(generic.FormView):
    template_name = 'users/recu-pass.html'
    form_class = ForgotPswd
    success_url = reverse_lazy('users:list-users')


    def form_valid(self, form):
        usuario = User.objects.get(id=self.kwargs['pk'])
        
        usuario.set_password(form.cleaned_data['password'])
        usuario.first_time = True
        usuario.save()
        return super(RecuPswd, self).form_valid(form)

