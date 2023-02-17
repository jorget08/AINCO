from django.urls import path

from . import views

app_name = 'biblioteca'

urlpatterns = [
    path(route = 'biblioteca', view = views.BibliotecaView.as_view(), name = 'biblio'),
]