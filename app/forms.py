from django.forms import ModelForm, TextInput
from app.models import Carro


# Create the form class.
class CarroForm(ModelForm):
     class Meta:
         model = Carro
         fields = ["imagem","modelo", "marca", "ano", "placa"]


# Creating a form to add an article.
#form = ArticleForm()

# Creating a form to change an existing article.
#article = Article.objects.get(pk=1)
#form = ArticleForm(instance=article)