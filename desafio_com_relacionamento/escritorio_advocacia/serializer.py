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
    parte = serializers.SlugRelatedField(
        many=False,
        slug_field='nome',
        read_only=False,
        queryset=Cliente.objects.all(),
    )
    responsavel = serializers.SlugRelatedField(
        many=False,
        slug_field='nome',
        read_only=False,
        queryset=Advogado.objects.all(),
    )

    class Meta:
        model = Processo
        fields = '__all__'
     
