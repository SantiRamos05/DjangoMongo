from django.urls import path
from proyectos import views

app_name = "accounts"
urlpatterns = [
    path('crear-proyecto/', views.CrearProyectos.as_view(), name="crear-proyecto"),

]   
