# Generated by Django 4.1 on 2022-09-08 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formsexemplo", "0005_jogador_pontos_na_temporada"),
    ]

    operations = [
        migrations.AddField(
            model_name="time",
            name="fundacao",
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
