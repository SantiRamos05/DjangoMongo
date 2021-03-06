from django import forms
from django.forms import widgets
from .models import Proyectos, ProyectoEmpleados, HistoriasUsuario

class CrearProyectos(forms.ModelForm):
    nombreclave = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}))
    fechainicio = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control','type':'date'}))
    fechafinalizacion = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control','type':'date'}))
    
    class Meta:
        model = Proyectos
        fields = ['nombreclave','fechainicio', 'fechafinalizacion', 'promotor', 'denominacioncomercial' ]

class AsignarEmpleadosProyecto(forms.ModelForm):

    class Meta:
        model = ProyectoEmpleados
        fields = ['empleados']
        widgets = {
            'empleados':forms.CheckboxSelectMultiple()
        }

class HistoriasUsuarioForm(forms.ModelForm):
    identificacionhistoriausuario = forms.CharField(widget=forms.NumberInput(attrs={'class':'border rounded-0 form-control'}))
    descripcionhistoriausuario = forms.CharField(widget=forms.Textarea(attrs={'class':'border rounded-0 form-control'}))
    
    class Meta:
        model = HistoriasUsuario
        fields = ['proyecto', 'identificacionhistoriausuario', 'descripcionhistoriausuario']


class AsignarTarea(forms.ModelForm):
    identificacionhistoriausuario = forms.CharField(widget=forms.NumberInput(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly'}))
    descripcionhistoriausuario = forms.CharField(widget=forms.Textarea(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly'}))
    fechainicioesperado = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly'}))
    fechainicioreal = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly'}))
    duracionesperada = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control','readonly':'readonly'}))
    duracionreal = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly'}))

    class Meta:
        model = HistoriasUsuario
        fields = ['identificacionhistoriausuario', 'descripcionhistoriausuario', 'fechainicioesperado', 'fechainicioreal', 'duracionesperada', 'duracionreal', 'empleados']
        widgets = {
            'empleados':forms.TextInput(attrs={'class':'border rounded-0 form-control', 'readonly':'readonly', 'hidden':True})
        }