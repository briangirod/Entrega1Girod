from django.db import models

# Create your models here.
class Incidencias(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    incidente= models.CharField(max_length=250)


class Solicitud(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    solicitud= models.CharField(max_length=250)

class Creacion(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    creacion= models.CharField(max_length=250)
    informacion= models.CharField(max_length=400)
