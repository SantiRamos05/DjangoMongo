from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearEmpleado

class CrearUsuario(LoginRequiredMixin, CreateView):
    model = User
    form_class =  CrearEmpleado
    template_name = 'accounts/crear-empleado.html'
    #toca arreglar esto
    success_url =  'Home'


