from django.db import models

# Create your models here.
class Carro(models.Model):
  
  modelo = models.CharField(max_length=50)
  marca = models.CharField(max_length=50)
  ano = models.IntegerField()
  placa = models.CharField(max_length=50)
  imagem = models.ImageField()

  
  