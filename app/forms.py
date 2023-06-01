from django import forms
from app.models import Carro, Teste


# Create the form class.
class CarroForm(forms.ModelForm):
     class Meta:
         model = Carro
         fields = ["imagem","modelo", "marca", "ano", "placa"]


class TesteForm(forms.ModelForm):
     class Meta:
        model = Teste
        fields = ["picture"]
# Creating a form to add an article.
#form = ArticleForm()

# Creating a form to change an existing article.
#article = Article.objects.get(pk=1)
#form = ArticleForm(instance=article)