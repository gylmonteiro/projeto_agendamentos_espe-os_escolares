# Generated by Django 4.2.6 on 2023-10-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("turmas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="turma",
            name="turma",
            field=models.CharField(default="A", max_length=1),
        ),
    ]
