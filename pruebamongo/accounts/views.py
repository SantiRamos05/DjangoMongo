from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearEmpleado

class CrearUsuario(LoginRequiredMixin, CreateView):
    model = User
    form_class =  CrearEmpleado
    template_name = 'accounts/crear-empleado.html'
    success_url = 'crear-empleado'


