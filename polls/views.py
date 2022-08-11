from django.shortcuts import redirect, render

from polls.models import Opcao, Questao

# Create your views here.
def index(request):
    questoes = Questao.objects.all()
    context = {
        'questoes': questoes,
    }
    return render(request, 'polls/index.html', context=context)


def questao(request, questao_id):
    q = Questao.objects.all().filter(pk=questao_id).first()

    context = {"questao": q}

    return render(request, "polls/questao.html", context=context)


def vota(request, opcao_id):
    opcao = Opcao.objects.filter(pk=opcao_id).first()

    opcao.votos = opcao.votos + 1

    opcao.save()

    return redirect(f"/polls/questao/{opcao.questao.id}/")
