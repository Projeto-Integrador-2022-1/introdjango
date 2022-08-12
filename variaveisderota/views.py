"""Exemplos de views que usam variáveis de rotas."""
from django.http import HttpResponse, HttpRequest

# from django.shortcuts import render

# Create your views here.
def diz_oi(request: HttpRequest, nome: str) -> HttpResponse:
    """Esta view receberá um nome qualquer e responderá com a frase de cordialidade."""
    return HttpResponse(f"Olá, {nome}! Como está?")


def intercaladas(
    request: HttpRequest, variavel_1: str, variavel_2: str
) -> HttpResponse:
    """Variáveis podem ser intercaladas na URL como pode observar no arquivo de urls."""
    return HttpResponse(f"Veja que funciona: {variavel_1}, {variavel_2}.")
