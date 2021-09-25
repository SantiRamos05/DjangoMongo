from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'pruebamongo/Login.html'

class Index(TemplateView):
    template_name= 'pruebamongo/base.html'