import uuid

from datetime import datetime
from django.db import models

# Create your models here.
POSICAO = (
    ("LIB", "Líbero"),
    ("LEV", "Levantador"),
    ("PON", "Ponteiro"),
    ("CEN", "Central"),
    ("OPO", "Oposto"),
)


class Time(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    fundacao = models.DateField(default=datetime.today)

    plantel = models.ManyToManyField('Jogador', related_name='times', through='Contrato', through_fields=('time', 'jogador'))

    def __str__(self) -> str:
        return self.nome


def user_directory_path(instance, filename):
    """Trouxe direto da documentação, para simplificar."""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user/{filename}"


class Jogador(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    altura = models.FloatField()
    peso = models.FloatField()
    data_nascimento = models.DateField("Data de nascimento")
    posicao = models.CharField("Posição", max_length=3, choices=POSICAO, default='CEN')
    eh_ruim = models.BooleanField("É ruim", default=True)

    pontos_na_temporada = models.IntegerField(default=0)

    foto = models.ImageField(
        "Foto de perfil", blank=True, upload_to=user_directory_path
    )

    def __str__(self) -> str:
        return self.nome

class Contrato(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    jogador = models.ForeignKey(Jogador, on_delete=models.DO_NOTHING, related_name="contratos")
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)

    inicio = models.DateField(default=datetime.today)
    final = models.DateField(default=datetime.today)

    salario = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"Contrato entre {self.jogador.nome} e o time {self.time.nome}"

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.id = uuid.uuid4()
        super(Contrato, self).save(*args, **kwargs)


class Doenca(models.Model):
    nome = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return self.nome

class HistoricoMedico(models.Model):
    jogador = models.OneToOneField(Jogador, on_delete=models.CASCADE, related_name="historico")
    doencas = models.ManyToManyField(Doenca, blank=True)

    def __str__(self) -> str:
        return f"Histórico médico do {self.jogador.nome} que joga."