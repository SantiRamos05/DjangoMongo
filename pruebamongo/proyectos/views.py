from accounts.models import User
from django.shortcuts import render
from .forms import CrearProyectos
from .models import Proyectos
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

# Create your views here.

class CrearProyectos(LoginRequiredMixin, CreateView):
    form_class = CrearProyectos
    model = Proyectos
    template_name = 'proyectos/crear-proyectos.html'
    #toca arreglar esto
    success_url = 'Home'

    def form_valid(self, form):
        promotor = form.cleaned_data.get('promotor')
        grupo_promotor = Group.objects.get(name = "Promotor")
        usuario = User.objects.get(username = promotor)
        print('Este es el usuario', usuario)
        print('Este es el grupo', grupo_promotor)
        usuario.groups = grupo_promotor
        usuario.save()
        return super().form_valid(form)
