from rest_framework import serializers

from app.models import Carro

class CarroSerialize(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields =  ['imagem','modelo', 'marca', 'ano', 'placa']
        
