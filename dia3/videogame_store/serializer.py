from rest_framework import serializers
from .models import Jogo, Loja, Cliente

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']