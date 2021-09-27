from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect

class Home(TemplateView):
    template_name = 'pruebamongo/Login.html'

class Index(TemplateView):
    template_name= 'pruebamongo/base.html'

def logout_site(request):
    logout(request)
    return HttpResponseRedirect('/')