from django.contrib import admin
from django.urls import path, include
from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='Home'),
    path('', include('accounts.urls', namespace='account')),
    path('', include('proyectos.urls', namespace='proyectos')),
]
