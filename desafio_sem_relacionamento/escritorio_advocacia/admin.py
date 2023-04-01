from django.contrib import admin
from .models import Processo, Advogado, Cliente


# Register your models here.


class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'area')
admin.site.register(Advogado, AdvogadoAdmin)
    

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email', 'telefone')
admin.site.register(Cliente, ClienteAdmin)
    
class ProcessosAdmin(admin.ModelAdmin):
    list_display = ('parte', 'numero', 'assunto', 'criacao', 'ativo', 'informacoes', 'responsavel')
admin.site.register(Processo, ProcessosAdmin)
