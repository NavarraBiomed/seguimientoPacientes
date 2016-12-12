# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0027_auto_20161212_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='alcohol',
            field=models.IntegerField(null=True, blank=True, max_length=2, choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')], verbose_name='Alcohol'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='rankinbasal',
            field=models.IntegerField(null=True, blank=True, choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')], verbose_name='Escala de Rankin'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tabaquismo',
            field=models.IntegerField(null=True, blank=True, max_length=2, choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')], verbose_name='Tabaco'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='rankin3m',
            field=models.IntegerField(null=True, blank=True, choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')], verbose_name='Escala de Rankin 3 meses'),
        ),
    ]
