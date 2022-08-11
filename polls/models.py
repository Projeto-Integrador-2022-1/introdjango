"""Entidades do projeto.
"""
from django.db import models

# Create your models here.
class Questao(models.Model):
    """Uma questão que será apresentada."""

    questao_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Questão: "{self.questao_texto}", publicada em {self.pub_date}'


class Opcao(models.Model):
    """Uma opção que pertence a uma questão."""

    questao = models.ForeignKey(
        Questao, on_delete=models.CASCADE, related_name="opcoes"
    )
    opcao_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Opção: "{self.opcao_text}" da questão "{self.questao.questao_texto}"'
