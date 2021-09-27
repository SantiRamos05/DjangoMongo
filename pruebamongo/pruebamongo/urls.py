from django.contrib import admin
from django.urls import path, include
from .views import Home, Index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name ='pruebamongo/Login.html', redirect_authenticated_user=True), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('home/', Index.as_view(), name='Home'),
    path('', include('accounts.urls', namespace='account')),
    path('', include('proyectos.urls', namespace='proyectos')),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )