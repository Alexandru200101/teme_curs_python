from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Autentificare & Înregistrare
    path('signup/', views.signup_view, name='signup'),
    path('login-firma/', views.login_view, name='login_firma'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards
    path('dashboard-firma/', views.dashboard_firma, name='dashboard_firma'),
    path('dashboard-superuser/', views.dashboard_superuser, name='dashboard_superuser'),

    # Operațiuni contabile
    path('adauga-operatiune/', views.adauga_operatiune, name='adauga_operatiune'),
    path('operatiuni/', views.lista_operatiuni, name='lista_operatiuni'),
]







