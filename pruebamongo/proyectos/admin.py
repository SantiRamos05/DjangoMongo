from django.contrib import admin
from .models import Proyectos
# Register your models here.
class AdminProyectos(admin.ModelAdmin):
    list_display = ['nombreclave', 'promotor', 'denominacioncomercial', 'estadoactual']

admin.site.register(Proyectos, AdminProyectos)
