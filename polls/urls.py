"""Rotas do módulo Polls."""
from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="index"),
    path("questao/<questao_id>/", views.questao, name="questao"),
    path("vota/<opcao_id>/", views.vota, name="vota"),
]
