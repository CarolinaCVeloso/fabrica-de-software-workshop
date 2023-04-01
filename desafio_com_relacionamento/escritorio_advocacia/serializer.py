from rest_framework import serializers
from .models import Advogado, Cliente, Processo

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProcessoSerializer(serializers.ModelSerializer):

    parte_nome = serializers.SerializerMethodField()

    responsavel_nome = serializers.SerializerMethodField()


    class Meta:
        model = Processo
        fields = '__all__'
     
    def get_parte_nome(self, obj):
        return obj.parte.nome

    def get_responsavel_nome(self, obj):
        return obj.responsavel.nome
