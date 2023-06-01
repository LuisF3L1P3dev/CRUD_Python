from django.db import models

# Create your models here.
class Carro(models.Model): 
  imagem = models.ImageField(blank=True, upload_to='uploads')
  modelo = models.CharField(max_length=50)
  marca = models.CharField(max_length=50)
  ano = models.IntegerField()
  placa = models.CharField(max_length=50)
  

class Teste(models.Model):
  picture = models.ImageField(blank="True", upload_to="image")