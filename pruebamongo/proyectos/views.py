from django.views.generic.detail import DetailView
from accounts.models import User
from django.shortcuts import redirect, render
from .forms import CrearProyectos
from .models import Proyectos, ProyectoEmpleados
from django.views.generic import CreateView, ListView
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
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.groups.id == 3:
                return super().dispatch(request, *args, **kwargs)
        return redirect('Home')

class ListarProyectos(LoginRequiredMixin, ListView):
    model = Proyectos
    template_name = 'proyectos/listar-proyectos.html'

class ListarEmpleadosProyecto(LoginRequiredMixin, DetailView):
    model = Proyectos
    template_name = 'proyectos/listar-empleados-proyecto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs['object']
        context['empleados']= ProyectoEmpleados.objects.filter(proyecto = id.id)
        return context
    
    
