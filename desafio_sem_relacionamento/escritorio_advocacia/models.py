from django.db import models



class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.DecimalField(max_digits=12, decimal_places=0);
    email = models.EmailField()
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100);
    endereco = models.CharField(max_length=150);
    email = models.EmailField()
    telefone = models.DecimalField(max_digits=12, decimal_places=0);

    def __str__(self):
        return self.nome

class Processo(models.Model):
    parte = models.CharField(max_length=100)
    responsavel = models.CharField(max_length = 100, verbose_name='Responsável')
    numero = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='Número Processo');
    assunto = models.CharField(max_length=100)
    informacoes = models.TextField(blank=True, default='', verbose_name='Informações')
    criacao = models.DateField(auto_created=True, verbose_name='Criação')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.parte