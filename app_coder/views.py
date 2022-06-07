from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Incidencias, Solicitud, Creacion
from django.template import loader
from app_coder.forms import form_crea, form_inc, form_sol

# Create your views here.


def inicio(request):

    return render (request, "index.html")


def creacion_formulario(request):

    if request.method == "POST":

        crea_formulario = form_crea( request.POST )

        if crea_formulario.is_valid():
            datos = crea_formulario.cleaned_data          
            
            creacion = Creacion( nombre=datos['nombre'] , apellido=datos['apellido'], creacion=datos['creacion'], informacion=datos['informacion'], )
            creacion.save()

            return render( request, "alta.html")

    return render( request, "creacion.html")

def incidencia_formulario(request):

    if request.method == "POST":

        inci_formulario = form_inc( request.POST )

        if inci_formulario.is_valid():
            datos = inci_formulario.cleaned_data          
            
            incidencia = Incidencias( nombre=datos['nombre'] , apellido=datos['apellido'], incidente=datos['incidente'] )
            incidencia.save()

            return render( request, "alta.html")

    return render( request, "incidencia.html")

def solicitud_formulario(request):

    if request.method == "POST":

        sol_formulario = form_sol( request.POST )

        if sol_formulario.is_valid():
            datos = sol_formulario.cleaned_data          
            
            solicitud = Solicitud( nombre=datos['nombre'] , apellido=datos['apellido'], solicitud=datos['solicitud'] )
            solicitud.save()

            return render( request, "alta.html")

    return render( request, "solicitud.html")

    
def alta(request):

    return render (request, "alta.html")


def buscar_inc(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        incidencia = Incidencias.objects.filter(nombre__icontains = nombre)
        return render( request , "resultados.html" , {"incidencia": incidencia})
    else:
        return HttpResponse("Campo vacio")


   
