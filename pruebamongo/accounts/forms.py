from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User

class CrearEmpleado(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'help_texts':None}),label= 'Usuario')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'help_texts':None}), label= 'Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'help_texts':None}), label= 'Repertir Contraseña')
    first_name = forms.CharField(widget=forms.PasswordInput(attrs={'help_texts':None}), label= 'Nombres')
    last_name = forms.CharField(widget=forms.PasswordInput(attrs={'help_texts':None}), label= 'Apellidos')
    email = forms.CharField(widget=forms.PasswordInput(attrs={'help_texts':None}), label= 'Correo Electronico')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'identificacion', 'direccion', 'telefono', 'groups']