from django.db import models

# Create your models here.
# arrayMarcas = [''] ? é melhor um array um uma classe para marcas?
#if carro = vai ter MarcaCarros else moto = MarcaMoto
class Marca(models.Model):
   nome = models.CharField(max_length=50)
   logo = models.ImageField(blank=True, upload_to='img_marcas')
   #um veciculo vai ter uma marca, uma marca vai ter varios veiculos 

class Veiculo(models.Model):
  class Meta:
      abstract = True
      
  VEICULO_CHOICE = (
    ("C", "Carro"),
    ("M", "Moto"),
    ("V", "Van"),
  )     
  tipo = models.CharField(max_length=1, choices=VEICULO_CHOICE, blank=False, null=False)
  modelo = models.CharField()
  marca = models.ForeignKey("Marca", on_delete=models.CASCADE, related_name='Veiculo')
  ano = models.DateField()
  placa = models.CharField()#o regex para placa pode ser feito na url
  
class Carro(Veiculo):
  pass
class Moto(Veiculo):
  pass