from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q

from .models import Bilbio

# Create your views here.

class BibliotecaView(LoginRequiredMixin, ListView):
    template_name = 'biblioteca/biblio.html'
    model = Bilbio
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        kword = self.request.GET.get("kword", '')
        context['biblio'] = Bilbio.objects.filter(Q(tema__icontains=kword))

        return context