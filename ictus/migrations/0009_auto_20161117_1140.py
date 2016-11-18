# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0008_auto_20161117_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='basal',
            name='chadsvasc',
            field=models.FloatField(verbose_name='CHADSVASC', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='episodio',
            name='acm_hiperdensa',
            field=models.CharField(verbose_name='ACM hiperdensa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='episodio',
            name='ait_bcd3',
            field=models.IntegerField(verbose_name='ABCD3', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='episodio',
            name='ait_previo',
            field=models.CharField(verbose_name='AIT', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='episodio',
            name='aspect_basal',
            field=models.FloatField(verbose_name='Puntuacion ASPECTS BASAL', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='episodio',
            name='clasif_sen',
            field=models.CharField(verbose_name='SEN', blank=True, choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')], null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='episodio',
            name='esus',
            field=models.CharField(verbose_name='ESUS', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='iniciomicro',
            field=models.FloatField(verbose_name='Tiempo inicio micro', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='iniciovena',
            field=models.FloatField(verbose_name='Tiempo inicio vena', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='mejoriaNIHSS4ev',
            field=models.IntegerField(verbose_name='ev -Mejoria de 4 puntos o mas en la escala nihss', blank=True, choices=[('00', 'No'), ('01', 'Sí')], null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='mejoriaNIHSS4ia',
            field=models.IntegerField(verbose_name='ia - Mejoria de 4 puntos o mas en la escala nihss', blank=True, choices=[('00', 'No'), ('01', 'Sí')], null=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='reacanalizacdtc',
            field=models.IntegerField(verbose_name='Recanalizacion durante rtpa', blank=True, choices=[('00', 'No'), ('01', 'Sí')], null=True),
        ),
    ]
