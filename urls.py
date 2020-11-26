from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index',views.index, name="index"),
    path('QuienesSomos',views.QuienesSomos, name="QuienesSomos"),
    path('registro', views.registro, name='registro'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),
    
]
