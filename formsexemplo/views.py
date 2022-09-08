from django.shortcuts import render

from formsexemplo.forms import FalaAihForm, NovaQuestao
from formsexemplo.models import Jogador

# Create your views here.
def home(request):
    formulario = FalaAihForm(request.POST or None)
    nquestao = NovaQuestao(request.POST or None)

    if request.method == 'POST':
        if formulario.is_valid():
            print(formulario.cleaned_data.get('resposta'))
        if nquestao.is_valid():
            nquestao.save()

    jogador = Jogador.objects.get(pk=1)

    context = {
        'form': formulario,
        'qform': NovaQuestao(),
        'jogador': jogador,
    }

    return render(request, 'formsexemplo/index.html', context=context)