from django.shortcuts import render
from .forms import CrearProyectos
from .models import Proyectos
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CrearProyectos(LoginRequiredMixin, CreateView):
    form_class = CrearProyectos
    model = Proyectos
    template_name = 'proyectos/crear-proyectos.html'
    success_url = 'accounts:crear-empleado'
