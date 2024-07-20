
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('logout/', views.logged_out, name='logged_out'),
    path('contact/', views.contact, name='contact'),
    path('exito/', views.exito, name='exito'),
    #path('login/', views.login, name='login'),

]











