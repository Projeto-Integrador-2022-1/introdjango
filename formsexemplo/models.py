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

    foto = models.ImageField(
        "Foto de perfil", blank=True, upload_to=user_directory_path
    )

    time = models.ForeignKey(Time, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        if self.time:
            return f"{self.nome} que joga no {self.time}"
        return f"{self.nome} está desempregado"


class Doenca(models.Model):
    nome = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return self.nome

class HistoricoMedico(models.Model):
    jogador = models.OneToOneField(Jogador, on_delete=models.CASCADE, related_name="historico")
    doencas = models.ManyToManyField(Doenca, blank=True)

    def __str__(self) -> str:
        return f"Histórico médico do {self.jogador.nome} que joga no {self.jogador.time}"