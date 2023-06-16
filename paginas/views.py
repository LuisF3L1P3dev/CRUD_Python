from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TesteView(TemplateView):
      template_name = "paginas/teste.html"

class SobreView(TemplateView):
      template_name = "paginas/sobre.html"