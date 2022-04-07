import threading
import base64

from datetime import date

from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template import loader

from .models import Gestion
from .forms import GestionForm, AddInfoForm, MailForm
from applications.gestionAbogado.forms import GestionAbogadoForm
from applications.gestionAbogado.models import GestionAbogado
from applications.actaDespacho.forms import ActaDespachoForm
from applications.actaDespacho.models import ActaDespacho
from applications.acuerdo.forms import AcuerdoForm, AcuedoActualizacion
from applications.acuerdo.models import AcuerdosPago
from applications.deudor.models import Deudor
from applications.credito.models import Credito
from applications.codeudor.models import Codeudor
from applications.conyugue.models import Conyugue
from applications.users.models import User
from applications.pago.models import Pagos
from applications.correos.tasks import send_mail_task
from applications.deudor.forms import CastigadaForm
from applications.adicional.models import Adicionado


#PDF
from applications.utils import render_to_pdf

# Create your views here.


class GestionView(LoginRequiredMixin, generic.CreateView):
    
    template_name = 'gestion/gestion.html'
    
    form_class = GestionForm
    
    success_url = reverse_lazy('users:dashboard')
    
    def get_queryset(self):
        
        queryset = Deudor.objects.all()
        
        return queryset
    
    def get_slug_field(self):
        
        slug_field = 'cedula'
        
        return slug_field
    
    def get_slug_url_kwarg(self):
        
        slug_url_kwarg = 'cedula'
        
        return slug_url_kwarg
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        deudor = self.get_object()
        
        context['gestion'] = Gestion.objects.filter(deudores = deudor).order_by('fecha_gestion')
        context['conyugue'] = Conyugue.objects.filter(deudor = deudor)
        context['credito'] = Credito.objects.filter(deudor = deudor).order_by('-fecha_corte')
        context['codeudor'] = Codeudor.objects.filter(deudores = deudor)
        context['gestion'] = Gestion.objects.filter(deudores = deudor)
        context['pagos'] = Pagos.objects.filter(deudores = deudor).order_by('-fecha_pago')
        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        context['acuerdo_pago'] = AcuerdosPago.objects.filter(deudores = deudor)
        context['adicionado'] = Adicionado.objects.filter(deudores = deudor).last()
        context['acuerdo'] = AcuerdoForm
        context['formulario'] = MailForm
        context['castigada'] = CastigadaForm
        
        #usuario = self.request.user
        #context['total_estar_al_dia'] = Deudor.objects.total_estar_al_dia(usuario)
        
        #Lamado de los campos que se modifican, llamandolos en el template por su .pk
        context['user'] = self.request.user
        context['deudo'] = deudor
        
        #import pdb; pdb.set_trace() #--> el debug
        return context


class GestionAbogadoView(LoginRequiredMixin, generic.CreateView):
    
    template_name = 'gestion/gestionAbogado.html'
    
    form_class = GestionAbogadoForm
    
    success_url = reverse_lazy('users:dashboardAbogado')
    
    def get_queryset(self):
        
        queryset = Deudor.objects.all()
        
        return queryset
    
    def get_slug_field(self):
        
        slug_field = 'cedula'
        
        return slug_field
    
    def get_slug_url_kwarg(self):
        
        slug_url_kwarg = 'cedula'
        
        return slug_url_kwarg
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        deudor = self.get_object()
        
        context['gestion'] = Gestion.objects.filter(deudores = deudor).order_by('fecha_gestion')
        context['conyugue'] = Conyugue.objects.filter(deudor = deudor)
        context['credito'] = Credito.objects.filter(deudor = deudor).order_by('-fecha_corte')
        context['codeudor'] = Codeudor.objects.filter(deudores = deudor)
        context['gestion'] = Gestion.objects.filter(deudores = deudor)
        context['pagos'] = Pagos.objects.filter(deudores = deudor).order_by('-fecha_pago')
        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        context['acuerdo_pago'] = AcuerdosPago.objects.filter(deudores = deudor)
        context['adicionado'] = Adicionado.objects.filter(deudores = deudor).last()
        context['acuerdo'] = AcuerdoForm
        context['formulario'] = MailForm
        context['castigada'] = CastigadaForm
        context['acta_despacho'] = ActaDespachoForm
        context['acta'] = ActaDespacho.objects.filter(deudor = deudor)
        context['actuaciones'] = GestionAbogado.objects.filter(deudores = deudor)
        #usuario = self.request.user
        #context['total_estar_al_dia'] = Deudor.objects.total_estar_al_dia(usuario)
        
        #Lamado de los campos que se modifican, llamandolos en el template por su .pk
        context['user'] = self.request.user
        context['deudo'] = deudor
        
        #import pdb; pdb.set_trace() #--> el debug
        return context




class AddInfo(LoginRequiredMixin, generic.CreateView):
    template_name = 'gestion/add-info.html'
    
    form_class = AddInfoForm
    
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        kword = self.kwargs['pk']

        context['conyugue'] = Conyugue.objects.context_conyugue(kword)
        context['codeudor'] = Codeudor.objects.context_codeudor(kword)
        context['deudor'] = Deudor.objects.context_deudor(kword)
        context['user'] = self.request.user

        #import pdb; pdb.set_trace()
        return context


class ActaDespachoView(LoginRequiredMixin, generic.CreateView):

    form_class = ActaDespachoForm
    
    success_url = reverse_lazy('users:dashboardAbogado')

    def get_queryset(self):
        
        queryset = Deudor.objects.all()
        
        return queryset
    
    def get_slug_field(self):
        
        slug_field = 'cedula'
        
        return slug_field
    
    def get_slug_url_kwarg(self):
        
        slug_url_kwarg = 'cedula'
        
        return slug_url_kwarg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["deudor"] = Deudor.objects.get(cedula=self.kwargs['pk'])
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        deudor = self.get_object()
        ActaDespacho.objects.create(
            fecha_acta = request.POST['fecha_acta'],
            num_radicacion = request.POST['num_radicacion'],
            clase_proceso = request.POST['clase_proceso'],
            num_despacho = request.POST['num_despacho'],
            nombre_despacho = request.POST['nombre_despacho'],
            juez_o_magistrado = request.POST['juez_o_magistrado'],
            direccions_despacho = request.POST['direccions_despacho'],
            ciudad_despacho = request.POST['ciudad_despacho'],
            tel_fijo = request.POST['tel_fijo'],
            tel_fijo2 = request.POST['tel_fijo2'],
            cel = request.POST['cel'],
            cel2 = request.POST['cel2'],
            email = request.POST['email'],
            email2 = request.POST['email2'],
            observaciones = request.POST['observaciones'],
            comentarios = request.POST['comentarios'],
            acta = request.FILES['acta'],
            deudor = deudor,
            user = self.request.user
        )

        return HttpResponseRedirect(
                reverse(
                    'gestion:gestionAbogado',
                    kwargs={'pk': deudor.pk}
                )
            )
    


class MasInfoGestion(LoginRequiredMixin, generic.DetailView):
    pass



class AcuerdoView2(LoginRequiredMixin, generic.CreateView):
    
    form_class = AcuerdoForm
    
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        context['user'] = self.request.user
        #import pdb; pdb.set_trace()
        return context


    def post(self, request, *args, **kwargs):
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        if self.request.POST.get('fecha_2') == '' and self.request.POST.get('valor_compromiso_2') == '':
            acuerdo, creado = AcuerdosPago.objects.update_or_create(
            deudores = deudor,
            defaults = {
                'valor_compromiso': self.request.POST.get('valor_compromiso'),
                'forma_pago': self.request.POST.get('forma_pago'),
                'evidencia': self.request.POST.get('evidencia'),
                'fecha_1': self.request.POST.get('fecha_1'),
                'fecha_2': None,
                'fecha_3': None,
                'valor_compromiso_2': None,
                'valor_compromiso_3' : None,
                'estado_del_acuerdo' : 'En proceso',
                'user': self.request.user,
                'deudores': deudor,
            }
            )
            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )

        elif self.request.POST.get('fecha_3') == '' and self.request.POST.get('valor_compromiso_3') == '':
            acuerdo, creado = AcuerdosPago.objects.update_or_create(
            deudores = deudor,
            defaults = {
                'valor_compromiso': self.request.POST.get('valor_compromiso'),
                'forma_pago': self.request.POST.get('forma_pago'),
                'evidencia': self.request.POST.get('evidencia'),
                'fecha_1': self.request.POST.get('fecha_1'),
                'fecha_2': self.request.POST.get('fecha_2'),
                'fecha_3': None,
                'valor_compromiso_2': self.request.POST.get('valor_compromiso_2'),
                'valor_compromiso_3' : None,
                'estado_del_acuerdo' : 'En proceso',
                'user': self.request.user,
                'deudores': deudor,
            }
            )
            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )

        else:
            acuerdo, creado = AcuerdosPago.objects.update_or_create(
            deudores = deudor,
            defaults = {
                'valor_compromiso': self.request.POST.get('valor_compromiso'),
                'forma_pago': self.request.POST.get('forma_pago'),
                'evidencia': self.request.POST.get('evidencia'),
                'fecha_1': self.request.POST.get('fecha_1'),
                'fecha_2': self.request.POST.get('fecha_2'),
                'fecha_3': self.request.POST.get('fecha_3'),
                'valor_compromiso_2': self.request.POST.get('valor_compromiso_2'),
                'valor_compromiso_3' : self.request.POST.get('valor_compromiso_3'),
                'estado_del_acuerdo' : 'En proceso',
                'user': self.request.user,
                'deudores': deudor,
            }
            )
            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )


class CastigarCartera(LoginRequiredMixin, generic.UpdateView):
    
    form_class = CastigadaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        if self.request.POST.get('castigado') == 'on':
            deudor.castigado = True
            deudor.save()

        return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )
    
class AcuerdoPagoIncumplido(LoginRequiredMixin, generic.UpdateView):

    form_class = AcuedoActualizacion

    #model = AcuerdosPago

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        return context
    
    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        acuerdo = AcuerdosPago.objects.filter(deudores = deudor).update(estado_del_acuerdo= 'Incumplido')
        
        return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )


class AcuerdoPagoCumplido(LoginRequiredMixin, generic.UpdateView):

    form_class = AcuedoActualizacion

    #model = AcuerdosPago

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        return context
    
    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        acuerdo = AcuerdosPago.objects.filter(deudores = deudor).update(estado_del_acuerdo= 'Cumplido')
        
        return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )

            

class EmailSend(LoginRequiredMixin, generic.TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        #import pdb; pdb.set_trace()
        return context

      
    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        subject = self.request.POST.get('subject')
        para = self.request.POST.get('para')           
        message = self.request.POST.get('message')
        de = self.request.POST.get('de')           
        passw = self.request.POST.get('pass_de')

        passwdd = base64.b64decode(passw)
        passwd = passwdd.decode('ascii')

        cc = self.request.POST.get("cc")

        carta = self.request.POST.get("carta")

        recipient_list=[para, cc]

        if carta == "0":
            send_mail(               
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passwd,
            )

            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )

        if carta == "1":
            html_email = loader.render_to_string(
            'gestion/carta1_deudor.html',
            {
                'deudor' : deudor,
                'fecha' : date.today(),
                'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
            }
            )

            send_mail(               
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passwd,
            html_message=html_email,
            )

            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )
        
        if carta == "2":
            html_email = loader.render_to_string(
            'gestion/carta2_deudor.html',
            {
                'deudor' : deudor,
                'fecha' : date.today(),
                'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
            }
            )

            send_mail(               
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passwd,
            html_message=html_email,
            )

            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )

        if carta == "3":
            html_email = loader.render_to_string(
            'gestion/carta3_deudor.html',
            {
                'deudor' : deudor,
                'fecha' : date.today(),
                'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
            }
            )

            send_mail(
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passwd,
            html_message=html_email,
            )

            return HttpResponseRedirect(
                reverse(
                    'gestion:gestion',
                    kwargs={'pk': deudor.pk}
                )
            )


class Carta1PdfDeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        today = date.today()
        data = {
            'deudor': deudor,
            'fecha': today,
            'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
        }
        pdf = render_to_pdf('gestion/carta1_deudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Carta2PdfDeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        today = date.today()
        data = {
            'deudor': deudor,
            'fecha': today,
            'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
        }
        pdf = render_to_pdf('gestion/carta2_deudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Carta3PdfDeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        today = date.today()
        data = {
            'deudor': deudor,
            'fecha': today,
            'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
        }
        pdf = render_to_pdf('gestion/carta3_deudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Carta1PdfCodeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        codeudor = Codeudor.objects.get(cedula=self.kwargs['pk'])
        credito = self.request.GET.get("credito", '')
        today = date.today()
        data = {
            'codeudor': codeudor,
            'fecha': today,
            'credito': Credito.objects.get(codigo_credito = credito)
        }
        pdf = render_to_pdf('gestion/carta1_codeudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Carta2PdfCodeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        codeudor = Codeudor.objects.get(cedula=self.kwargs['pk'])
        credito = self.request.GET.get("credito", '')
        today = date.today()
        data = {
            'codeudor': codeudor,
            'fecha': today,
            'credito': Credito.objects.get(codigo_credito = credito)
        }
        pdf = render_to_pdf('gestion/carta2_codeudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Carta3PdfCodeudor(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        codeudor = Codeudor.objects.get(cedula=self.kwargs['pk'])
        credito = self.request.GET.get("credito", '')
        today = date.today()
        data = {
            'codeudor': codeudor,
            'fecha': today,
            'credito': Credito.objects.get(codigo_credito = credito)
        }
        pdf = render_to_pdf('gestion/carta3_codeudor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

