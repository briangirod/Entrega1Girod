from django import forms


class form_inc(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    incidente= forms.CharField(max_length=250)


class form_sol(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    solicitud= forms.CharField(max_length=250)

class form_crea(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    creacion= forms.CharField(max_length=250)
    informacion= forms.CharField(max_length=400)
