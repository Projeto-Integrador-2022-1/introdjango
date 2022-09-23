"""Views do módulo principal.

As views principais estão aqui.
"""
from django.shortcuts import render


def home(request):
    """Rota principal do site."""
    mensagem = ''
    if 'next' in request.GET:
        mensagem = "Você veio parar aqui pq tentou acessar algo que não devia."

    context = {
        'mensagem': mensagem,
    }

    return render(request, 'index.html', context=context)
