from django.contrib import admin
from django.urls import path, include
from .views import Home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='Home'),
    path('', include('accounts.urls', namespace='account')),
    path('', include('proyectos.urls', namespace='proyectos')),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )