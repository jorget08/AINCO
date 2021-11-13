import threading

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
from applications.acuerdo.forms import AcuerdoForm
from applications.acuerdo.models import AcuerdosPago
from applications.deudor.models import Deudor
from applications.credito.models import Credito
from applications.codeudor.models import Codeudor
from applications.conyugue.models import Conyugue
from applications.users.models import User
from applications.pago.models import Pagos
from applications.correos.tasks import send_mail_task

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
        context['acuerdo'] = AcuerdoForm
        context['formulario'] = MailForm

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

    

class EmailSend(LoginRequiredMixin, generic.TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['deudor'] = Deudor.objects.get(cedula=self.kwargs['pk'])
        #import pdb; pdb.set_trace()
        return context

      
    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        para = []
        deudor = Deudor.objects.get(cedula=self.kwargs['pk'])
        subject = self.request.POST.get('subject')
        para = self.request.POST.get('para')           
        message = self.request.POST.get('message')
        de = self.request.POST.get('de')           
        passw = self.request.POST.get('pass_de')
        html_email = loader.render_to_string(
            'gestion/carta1_deudor.html',
            {
                'deudor' : deudor,
                'fecha' : date.today(),
                'creditos': Credito.objects.filter(deudor = deudor).filter(normalizado = False)
            }
        )    

        #send_mail_task.delay(subject, message, de, para, passw, html_email)
        send_mail(               
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passw,
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

