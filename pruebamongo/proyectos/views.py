from django.http import request
import proyectos
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from accounts.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AsignarEmpleadosProyecto, AsignarTarea, CrearProyectos, HistoriasUsuarioForm
from .models import HistoriasUsuario, Proyectos, ProyectoEmpleados
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

# Create your views here.

class CrearProyectos(LoginRequiredMixin, CreateView):
    form_class = CrearProyectos
    model = Proyectos
    template_name = 'proyectos/crear-proyectos.html'

    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        promotor = form.cleaned_data.get('promotor')
        grupo_promotor = Group.objects.get(name = "Promotor")
        usuario = User.objects.get(username = promotor)
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

class AsignarEmpleadoProyectoView(LoginRequiredMixin, UpdateView):
    form_class = AsignarEmpleadosProyecto
    model = ProyectoEmpleados
    template_name = 'proyectos/asignar-empleado-proyecto.html'
    success_url = reverse_lazy('Home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.groups.id == 3 or request.user.groups.id == 2:
                return super().dispatch(request, *args, **kwargs)
        return redirect('Home')

class CrearHistoriaUsuario(LoginRequiredMixin, CreateView):
    model = HistoriasUsuario
    form_class = HistoriasUsuarioForm
    template_name = 'proyectos/crear-historia-usuario.html'
    success_url = reverse_lazy('Home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.groups.id == 2:
                return super().dispatch(request, *args, **kwargs)
        return redirect('Home')

class ListarProyectosUsuaro(LoginRequiredMixin, ListView):
    model = ProyectoEmpleados
    template_name = "proyectos/listar-proyectos-empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try: 
            proyectoempleado = ProyectoEmpleados.objects.get(empleados = self.request.user)
        except:
            proyectoempleado = None
        if proyectoempleado != None:
            context["proyectos"] = Proyectos.objects.filter(nombreclave = proyectoempleado.proyecto)
        
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.groups.id == 1:
                return super().dispatch(request, *args, **kwargs)
        return redirect('Home')


class ListarTareasProyecto(LoginRequiredMixin, ListView):
    model = HistoriasUsuario
    template_name = 'proyectos/list-tareas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proyecto = Proyectos.objects.get(id = self.kwargs['pk'])
        context['tareas'] = HistoriasUsuario.objects.filter(proyecto = proyecto.id)
        return context


class AsignarEmpleadoTarea(LoginRequiredMixin, UpdateView):
    model = HistoriasUsuario
    form_class = AsignarTarea

    template_name = 'proyectos/asignar-tarea.html'
    success_url = reverse_lazy('Home')

    def get_initial(self):
        initial = super(AsignarEmpleadoTarea, self).get_initial()
        user = User.objects.get(username= self.request.user)
        initial['empleados'] = user
        return initial
    


    
    
"""     def form_valid(self, form):
        empleado = User.objects.get(username = self.request.user)
        print(empleado)
        historia = HistoriasUsuario.objects.filter(empleados = empleado)


        #usuario.groups = grupo_promotor
        #usuario.save()
        return super().form_valid(form) """
    

    

