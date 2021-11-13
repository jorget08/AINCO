from django.urls import path

from . import views

app_name = 'gestion'

urlpatterns = [
    path(route = '<int:pk>', view = views.GestionView.as_view(), name = 'gestion'),

    path(route = 'add-info/<int:pk>', view = views.AddInfo.as_view(), name = 'add-info'),

    path(route = 'acuerdo/<int:pk>', view = views.AcuerdoView2.as_view(), name = 'acuerdo'),

    path(route = 'carta1/<int:pk>', view = views.Carta1PdfDeudor.as_view(), name = 'carta1_deudor'),

    path(route = 'carta2/<int:pk>', view = views.Carta2PdfDeudor.as_view(), name = 'carta2_deudor'),

    path(route = 'carta3/<int:pk>', view = views.Carta3PdfDeudor.as_view(), name = 'carta3_deudor'),
    
    path(route = 'carta3/<int:pk>/carta/', view = views.Carta1PdfCodeudor.as_view(), name = 'carta1_codeudor'),

    path(route = 'carta3/<int:pk>/carta/', view = views.Carta2PdfCodeudor.as_view(), name = 'carta2_codeudor'),

    path(route = 'carta3/<int:pk>/carta/', view = views.Carta3PdfCodeudor.as_view(), name = 'carta3_codeudor'),

    path(route = 'email/<int:pk>', view = views.EmailSend.as_view(), name = 'email'),

]