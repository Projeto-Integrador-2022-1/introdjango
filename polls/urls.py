"""Rotas do módulo Polls."""
from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="questaoindex"),
    path("questao/<questao_id>/", views.questao, name="questao"),
    path("escolhe/<opcao_id>/", views.vota, name="vota"),
]
