from django import forms
from django.forms import widgets

from .models import Proyectos, ProyectoEmpleados

class CrearProyectos(forms.ModelForm):
    fechainicio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2021-09-30'}))
    fechafinalizacion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2021-09-30'}))
    class Meta:
        model = Proyectos
        fields = ['nombreclave', 'promotor', 'denominacioncomercial', 'fechainicio', 'fechafinalizacion']

class AsignarEmpleadosProyecto(forms.ModelForm):

    class Meta:
        model = ProyectoEmpleados
        fields = ['empleados']
        widgets = {
            'empleados':forms.CheckboxSelectMultiple()
        }