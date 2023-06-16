from django.shortcuts import render, redirect
from django.views import View
from app.forms import CarroForm, TesteForm
from app.models import Carro, Teste
from django.core.paginator import Paginator
from rest_framework import viewsets
from PIL import Image

from app.serialize import CarroSerialize

# Create your views here.
def home(request):
    data = {
        #'db': Carro.objects.all()
    }
    # busca
    # ainda não esá funcionando pois esta dando conflito com a paginação
    search = request.GET.get("search")
    if search:
        data["db"] = Carro.objects.filter(modelo__icontains=search)
    else:
        data["db"] = Carro.objects.all()
    """ get context data """

    # paginação
    all = Carro.objects.all()
    paginator = Paginator(all, 4)  # numero de objetos na pagina
    pages = request.GET.get("page")
    data["db"] = paginator.get_page(pages)
    return render(request, "index.html", data)

    """ estou tentando trocar paginator para a chave pg para não entrar em conflito com a chave db do dicionario data """
    """ https://acervolima.com/python-upload-de-imagens-em-django/ """


def form(request):
    context = {"form": CarroForm()}
    print(request.FILES)
    """ if request.method == 'POST': 
    form = CarroForm(request.POST, request.FILES) 
  if form.is_valid(): 
    form.save() 
    return redirect('home') 
  else: 
    form = CarroForm() """

    return render(request, "form.html", context)


def create(request):
    form = CarroForm(
        request.POST or None, request.FILES or None
    )  # por se usar classe base view é tem que colocar o metodo Files para as imagens serem baixadas em media
    if form.is_valid():
        form.save()
        return redirect("home")


def view(request, pk):
    context = {"db": Carro.objects.get(pk=pk)}
    return render(request, "view.html", context)


def edit(request, pk):
    context = {
        "db": Carro.objects.get(pk=pk),
    }
    context["form"] = CarroForm(instance=context["db"])
    return render(request, "form.html", context)
    """ data = {}
  data['db'] = Carro.objects.get(pk=pk)
  data['form'] = CarroForm(instance=data['db'])
  return render(request, 'form.html', data) """


def update(request, pk):
    context = {}
    context["db"] = Carro.objects.get(pk=pk)
    form = CarroForm(
        request.POST or None, request.FILES or None, instance=context["db"]
    )
    if form.is_valid():
        form.save()
        """  return render(request,'index.html') """
        return redirect("home")


def delete(request, pk):
    db = Carro.objects.get(pk=pk)
    db.delete()
    return redirect("home")


""" def teste(request):
    context = {"form": TesteForm()}
    form = TesteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "teste.html", context)
 """

class CarroViewsSet(viewsets.ModelViewSet):
    serializer_class = CarroSerialize
    queryset = Carro.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
