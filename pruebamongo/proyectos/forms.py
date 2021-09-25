from django import forms
from .models import Proyectos, ProyectoEmpleados, HistoriasUsuario

class CrearProyectos(forms.ModelForm):
    nombreclave = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}))
    fechainicio = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control','placeholder':'2021-09-30'}))
    fechafinalizacion = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control','placeholder':'2021-09-30'}))
    
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
        fields = ['identificacionhistoriausuario', 'descripcionhistoriausuario', 'documentacion']