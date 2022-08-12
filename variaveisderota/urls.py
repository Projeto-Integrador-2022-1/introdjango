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
]
