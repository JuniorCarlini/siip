from django.contrib import admin
from .models import Proprietario, Propriedade, Armadilha

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numero_telefone', 'email')

@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('nome_propriedade', 'proprietario', 'endereco',)

@admin.register(Armadilha)
class ArmadilhaAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'propriedade', 'coordenadas_geograficas', 'horario_ultima_sincronizacao')
