# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0012_auto_20161118_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='grupo_etnico',
            new_name='grupoetnico',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='genero',
            new_name='sexo',
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(null=True, blank=True, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='mejoriaNIHSS4ev',
            field=models.IntegerField(null=True, choices=[('00', 'No'), ('01', 'Sí')], blank=True, verbose_name='EV -Mejoria de 4 puntos o mas en la escala nihss'),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='mejoriaNIHSS4ia',
            field=models.IntegerField(null=True, choices=[('00', 'No'), ('01', 'Sí')], blank=True, verbose_name='IA - Mejoria de 4 puntos o mas en la escala nihss'),
        ),
    ]
