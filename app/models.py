from django.db import models

# Create your models here.
class Carro(models.Model): 
  imagem = models.ImageField(blank=True, upload_to='uploads', default="media/uploads/padraoCarro.jpg")
  modelo = models.CharField(max_length=50)
  marca = models.CharField(max_length=50)
  ano = models.IntegerField()
  placa = models.CharField(max_length=50)
  

""" @Carro
def get_imagem_url(self):
    if self.imagem and hasattr(self.imagem, 'url'):
       return self.imagem.url
    else:
       return "./media/image/padraoCarro.jpg" """
@Carro
def get_imagem_url(self):
  try:
    url = self.imagem.url
  except:
    url=''
  return url
    

class Teste(models.Model):
  picture = models.ImageField(blank="True", upload_to="image")