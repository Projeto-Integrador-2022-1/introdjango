from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from formsexemplo.forms import FalaAihForm, NovaQuestao, TimeForm
from formsexemplo.models import Jogador, Time

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


@login_required
@permission_required('formsexemplo.add_time', login_url='/')
def times(request):
    novo_time = TimeForm(request.POST or None)

    mensagem_erro = ''
    if novo_time.is_valid():
        fundacao = novo_time.cleaned_data['fundacao']
        nome = novo_time.cleaned_data['nome']
        if fundacao < date.today() \
            and fundacao > date(1850, 1, 1) \
            and "Hitler" not in nome:
            novo_time.save()
        else:
            mensagem_erro = 'Deixa de ser burro.'

    todos_os_times = Time.objects.all().order_by('fundacao')

    context = {
        'form': novo_time,
        'erro': mensagem_erro,
        'times': todos_os_times,
    }

    return render(request, 'formsexemplo/times.html', context=context)