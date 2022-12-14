# Generated by Django 4.1.2 on 2022-10-19 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lugar",
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
                ("nome", models.CharField(max_length=255)),
                ("endereco", models.CharField(max_length=255)),
                ("esporte", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Agendamento",
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
                ("inicio", models.DateTimeField()),
                ("fim", models.DateTimeField()),
                (
                    "localidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="boraApp.lugar"
                    ),
                ),
            ],
        ),
    ]
