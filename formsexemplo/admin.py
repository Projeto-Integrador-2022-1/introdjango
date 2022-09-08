from django.contrib import admin

from formsexemplo.models import Jogador, Time, HistoricoMedico, Doenca, Contrato

# Register your models here.
admin.site.register(Jogador)
admin.site.register(Time)
admin.site.register(HistoricoMedico)
admin.site.register(Doenca)
admin.site.register(Contrato)
