from django.contrib import admin

# Register your models here.
from .models import Carro, Teste

admin.site.register(Carro)
admin.site.register(Teste)
