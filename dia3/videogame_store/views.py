from django.shortcuts import render
from rest_framework import viewsets
from .serializer import JogoSerializer, LojaSerializer
from .models import Loja , Jogo


# Create your views here.

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
