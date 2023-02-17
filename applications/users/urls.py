from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(route = '', view = views.LoginView.as_view(), name='login'),
    
    path(route = 'dashboard', view = views.DashboardView.as_view(), name = 'dashboard'),
    
    path(route = 'logout', view =  views.LogoutView.as_view(), name = 'logout'),

    #Registrar un usuario
    path(route = 'registrar/nv/u/a', view =  views.UserRegisterView.as_view(), name = 'registrar'),

    path(route = 'change/pwd', view =  views.ChangePwd.as_view(), name = 'change-password'),

    path(route = 'list/a/u/x', view =  views.UsersList.as_view(), name = 'list-users'),

    path(route = 'recu/contra/<int:pk>', view =  views.RecuPswd.as_view(), name = 'change'),
    
    path(route = 'agendar', view =  views.AgendarView.as_view(), name = 'agendar'),

    path(route = 'castigados', view =  views.EntregaCarteraCastigada.as_view(), name = 'castigo'),

    path(route = 'dashboard/abogado', view =  views.DashboardAbogadoView.as_view(), name = 'dashboardAbogado'),

]