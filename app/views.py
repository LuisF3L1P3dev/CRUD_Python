from django.shortcuts import render, redirect
from app.forms import CarroForm
from app.models import Carro
from django.core.paginator import Paginator
from rest_framework import viewsets

from app.serialize import CarroSerialize

# Create your views here.
def home(request):
  data = {
    #'db': Carro.objects.all(),
  }
  all = Carro.objects.all()
  paginator = Paginator(all, 2)
  pages = request.GET.get('page')
  data['db'] = paginator.get_page(pages)
  return render(request, 'index.html', data)

def form(request):
  context={
    'form': CarroForm() 
  }
  return render(request, 'form.html', context)

def create(request):
  form = CarroForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('home')

def view(request, pk):
  context={
    'db': Carro.objects.get(pk=pk)
  }
  return render(request,'view.html', context)

def edit(request, pk):
  context ={
    'db': Carro.objects.get(pk=pk),
  }
  context['form'] = CarroForm(instance=context['db'])
  return render(request, 'form.html', context)
  """ data = {}
  data['db'] = Carro.objects.get(pk=pk)
  data['form'] = CarroForm(instance=data['db'])
  return render(request, 'form.html', data) """

def update(request, pk):
  context={}
  context['db']= Carro.objects.get(pk=pk)
  form = CarroForm(request.POST or None, instance=context['db'])
  if form.is_valid():
    form.save()
    """  return render(request,'index.html') """
    return redirect('home')

def delete(request, pk):
  db = Carro.objects.get(pk=pk)
  db.delete()
  return redirect('home')

class CarroViewsSet(viewsets.ModelViewSet):
  serializer_class = CarroSerialize
  queryset = Carro.objects.all()
  
  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)
  

