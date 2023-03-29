from rest_framework import serializers
from .models import Jogo, Loja

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']