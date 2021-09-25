from django.urls import path
from accounts import views

app_name = "accounts"
urlpatterns = [
    path('crear-empleado/', views.CrearUsuario.as_view(), name="crear-empleado"),
    
    #path('eliminar-empleados/', views.EliminarEmpleados.as_view(), name="eliminar-empleado"),
]
