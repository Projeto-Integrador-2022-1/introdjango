# Generated by Django 4.1 on 2022-09-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jogador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                ("altura", models.FloatField()),
                ("peso", models.FloatField()),
                (
                    "data_nascimento",
                    models.DateField(verbose_name="Data de nascimento"),
                ),
                (
                    "posicao",
                    models.CharField(
                        choices=[
                            ("LIB", "Líbero"),
                            ("LEV", "Levantador"),
                            ("PON", "Ponteiro"),
                            ("CEN", "Central"),
                            ("OPO", "Oposto"),
                        ],
                        default="CEN",
                        max_length=3,
                        verbose_name="Posição",
                    ),
                ),
                ("eh_ruim", models.BooleanField(default=True, verbose_name="É ruim")),
            ],
        ),
    ]