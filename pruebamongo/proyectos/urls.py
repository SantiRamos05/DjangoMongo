from django.urls import path
from proyectos import views

app_name = "accounts"
urlpatterns = [
    path('crear-proyecto/', views.CrearProyectos.as_view(), name="crear-proyecto"),
    path('listar-proyectos/', views.ListarProyectos.as_view(), name="listar-proyectos"),
    path('listar-empleados/<pk>', views.ListarEmpleadosProyecto.as_view(), name="listar-empleados"),
    path('asignar-empleado/<pk>/', views.AsignarEmpleadoProyectoView.as_view(), name="asignar-empleado"),
    path('crear-historia-usuario', views.CrearHistoriaUsuario.as_view(), name="crear-historia"),
    path('listar-mis-proyectos', views.ListarProyectosUsuaro.as_view(), name="listar-proyectos-usuario"),
    path('listar-mis-tareas/<pk>/', views.ListarTareasProyecto.as_view(), name="listar-mis-tareas"),
    path('unir-tarea/<pk>/', views.AsignarEmpleadoTarea.as_view(), name="asignar-tarea"),
]   
