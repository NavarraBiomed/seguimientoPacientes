# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0017_auto_20161201_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='grupoetnico',
            field=models.IntegerField(blank=True, choices=[('0', 'Caucásico mediterráneo'), ('1', 'Otro caucásico'), ('2', 'Latinoamericano-caribeño'), ('3', 'Asiático'), ('4', 'Negro o afro-americano'), ('5', 'Otra raza'), ('6', 'No determinado')], null=True, verbose_name='Grupo étnico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.IntegerField(choices=[('0', 'Hombre'), ('1', 'Mujer')], verbose_name='Sexo'),
        ),
    ]
