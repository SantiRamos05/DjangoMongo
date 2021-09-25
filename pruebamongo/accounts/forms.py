from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User

class CrearEmpleado(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Usuario')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border rounded-0 form-control'}), label= 'Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border rounded-0 form-control'}), label= 'Repertir Contraseña')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Nombres')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Apellidos')
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Correo Electronico')
    identificacion = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Identificacion')
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Direccion')
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded-0 form-control'}), label= 'Telefono')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'identificacion', 'direccion', 'telefono', 'groups']