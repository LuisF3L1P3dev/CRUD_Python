from django.shortcuts import render, redirect
from app.forms import CarroForm
from app.models import Carro

# Create your views here.
def home(request):
  data = {
    'db': Carro.objects.all()  
  }
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
    'form': CarroForm(instance=context['db'])
  }
  return render(request, 'form.html', context)

def update(request, pk):
  return render(request='index.html')