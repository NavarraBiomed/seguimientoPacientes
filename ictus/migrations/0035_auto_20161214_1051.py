# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0034_auto_20161214_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='rankinbasal',
            field=models.IntegerField(choices=[(0, 'Sin síntomas'), (1, 'Sin incapacidad importante'), (2, 'Incapacidad leve'), (3, 'Incapacidad moderada'), (4, 'Incapacidad moderadamente grave'), (5, 'Incapacidad grave'), (6, 'Muerte')], blank=True, null=True, verbose_name='Escala de Rankin'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='rankin3m',
            field=models.IntegerField(choices=[(0, 'Sin síntomas'), (1, 'Sin incapacidad importante'), (2, 'Incapacidad leve'), (3, 'Incapacidad moderada'), (4, 'Incapacidad moderadamente grave'), (5, 'Incapacidad grave'), (6, 'Muerte')], blank=True, null=True, verbose_name='Escala de Rankin 3 meses'),
        ),
    ]
