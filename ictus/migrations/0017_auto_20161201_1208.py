# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0016_auto_20161201_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='grupoetnico',
            field=models.FloatField(verbose_name='Grupo étnico', choices=[('00', 'Caucásico mediterráneo'), ('01', 'Otro caucásico'), ('02', 'Latinoamericano-caribeño'), ('03', 'Asiático'), ('04', 'Negro o afro-americano'), ('05', 'Otra raza'), ('06', 'No determinado')], max_length=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.FloatField(verbose_name='Sexo', max_length=2, choices=[('00', 'Hombre'), ('01', 'Mujer')]),
        ),
    ]
