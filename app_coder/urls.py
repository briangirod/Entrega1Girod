
from django.urls import path
from . import views

urlpatterns = [

    path("", views.inicio),
    path("incidente", views.incidencia_formulario, name="Incidencia"),
    path("solicitud", views.solicitud_formulario, name="Solicitud"),
    path("creacion", views.creacion_formulario, name="Creacion"),
    path("alta", views.alta , name="alta"),
    path("buscar_inc", views.buscar_inc)
]