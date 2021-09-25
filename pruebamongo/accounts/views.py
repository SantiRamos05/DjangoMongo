from django.shortcuts import redirect, render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.views.generic.list import ListView
from .models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearEmpleado

class CrearUsuario(LoginRequiredMixin, CreateView):
    model = User
    form_class =  CrearEmpleado
    template_name = 'accounts/crear-empleado.html'
    
    #toca arreglar esto
    success_url =  reverse_lazy('Home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.groups.id == 3:
                return super().dispatch(request, *args, **kwargs)
        return redirect('Home')
    


class EliminarEmpleados(LoginRequiredMixin, DeleteView):
    pass

