from datetime import datetime

from django.contrib import admin

from formsexemplo.models import Jogador, Time, HistoricoMedico, Doenca, Contrato

# Register your models here.
@admin.action(description='Melhorou')
def melhorou(modeladmin, request, queryset):
    queryset.update(eh_ruim=False)


class JogadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'altura', 'peso', 
                    'posicao', 'data_nascimento',
                    'eh_ruim', 'ganhos', 'foto']
    list_filter = ['posicao', 'eh_ruim']
    search_fields = ['nome', 'id']
    ordering = ["nome"]

    actions = [melhorou]

    def ganhos(self, obj):
        contratos = Contrato.objects.filter(jogador=obj, final__gt=datetime.today())

        salario_total = 0

        for contrato in contratos:
            salario_total = salario_total + contrato.salario
        
        return salario_total


class ContratoAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'jogador', 'time', 'inicio', 'final', 'salario_formatado']

    def salario_formatado(self, obj):
        return f'R$ {obj.salario}'


class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fundacao', 'total_jogadores', 'salarios']

    def total_jogadores(self, obj):
        return len(Contrato.objects.filter(time=obj, final__gt=datetime.today()))

    def salarios(self, obj):
        gastos = 0
        for jogador in obj.plantel.all():
            contratos = Contrato.objects.filter(time=obj, jogador=jogador, final__gt=datetime.today())

            for contrato in contratos:
                if contrato:
                    gastos = gastos + contrato.salario
        return gastos


admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(HistoricoMedico)
admin.site.register(Doenca)
admin.site.register(Contrato, ContratoAdmin)
