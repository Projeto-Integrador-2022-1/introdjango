"""Configurações das rotas para usar variáveis de rota."""
from django.urls import path

from variaveisderota import views

urlpatterns = [
    path("oi/<nome>/", views.diz_oi, name="dizoi"),
    path(
        "intercaladas/<variavel_1>/aqui/<variavel_2>/",
        views.intercaladas,
        name="intercaladas",
    ),
    path("calcule/<valor1>/<operador>/<valor2>/", views.calcule, name="calculadora"),
    path("query/", views.queryParams, name="queryparams"),
]
