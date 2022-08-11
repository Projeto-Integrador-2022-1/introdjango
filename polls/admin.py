from django.contrib import admin

from polls.models import Opcao, Questao

# Register your models here.
admin.site.register(Questao)
admin.site.register(Opcao)
