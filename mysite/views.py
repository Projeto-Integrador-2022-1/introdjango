"""Views do módulo principal.

As views principais estão aqui.
"""
from django.shortcuts import render


def home(request):
    """Rota principal do site."""
    return render(request, 'index.html')
