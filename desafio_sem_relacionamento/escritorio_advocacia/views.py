from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AdvogadoSerializer, ClienteSerializer, ProcessoSerializer
from .models import Advogado, Cliente, Processo


# Create your views here.

class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer

