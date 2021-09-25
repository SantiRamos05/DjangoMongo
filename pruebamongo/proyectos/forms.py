from django import forms
from .models import Proyectos

class CrearProyectos(forms.ModelForm):
    fechainicio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2021-09-30'}))
    fechafinalizacion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2021-09-30'}))
    class Meta:
        model = Proyectos
        fields = ['nombreclave', 'promotor', 'denominacioncomercial', 'fechainicio', 'fechafinalizacion']