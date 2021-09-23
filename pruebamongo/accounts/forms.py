from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CrearEmpleado(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'identificacion', 'direccion', 'telefono', 'groups']
