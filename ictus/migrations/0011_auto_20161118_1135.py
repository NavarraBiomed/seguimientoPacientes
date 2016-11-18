# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0010_auto_20161117_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seguimiento',
            name='variable_seguimiento',
        ),
        migrations.AddField(
            model_name='basal',
            name='toast_ictus_previo',
            field=models.CharField(verbose_name='TOAST ictus previo', null=True, max_length=2, choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')], blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='aterovb',
            field=models.IntegerField(verbose_name='Esteniosis VB significativa sintomática (ipsilateral al lado sintomático)', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='deterioro',
            field=models.IntegerField(verbose_name='Deterioro', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='dimerod',
            field=models.FloatField(verbose_name='Dimero D', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='duplex_dtc_ipsilateral',
            field=models.IntegerField(verbose_name='ESTENOSIS SIGNFICATIVAipsilateral (Vps >155 cm/s)', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='duplex_dtc_otro',
            field=models.IntegerField(verbose_name='ESTENOSIS significativa a cualquier otro nivel (vPS >155 CM/S)', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecocardio_cardioembolico',
            field=models.IntegerField(verbose_name='Ecocardio cardioembólico', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecocardio_fecha',
            field=models.DateField(verbose_name='Fecha de ecocardio', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecocardio_hallazgos',
            field=models.CharField(verbose_name='Hallazgos ecocardio', null=True, max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecocardio_hecho',
            field=models.IntegerField(verbose_name='Ecocardio realizado', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecodilatacion_ai',
            field=models.IntegerField(verbose_name='Dilatación auricular izquierda', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecosta_50_ipsi',
            field=models.IntegerField(verbose_name='ECOTSA>50% ipsilatearl', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecotsa_contra',
            field=models.IntegerField(verbose_name='Hallazgos ECOTSA contralateral', null=True, blank=True, choices=[(0, 'Normal'), (1, 'Ateromatosis carotidea sin estenosis'), (2, 'estenosis < 50%'), (3, 'estenosis  moderada 51 - 69 %'), (4, 'estenosis severa o critica (70-90 %)'), (5, 'estenosis critica (>90 %)'), (6, 'oclusion o estenosis suboclusiva')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='ecotsa_ipsi',
            field=models.IntegerField(verbose_name='Hallazgos ECOTSA ipsilateral', null=True, blank=True, choices=[(0, 'Normal'), (1, 'Ateromatosis carotidea sin estenosis'), (2, 'estenosis < 50%'), (3, 'estenosis  moderada 51 - 69 %'), (4, 'estenosis severa o critica (70-90 %)'), (5, 'estenosis critica (>90 %)'), (6, 'oclusion o estenosis suboclusiva')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='fluctuacion',
            field=models.IntegerField(verbose_name='Fluctuación', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='holter',
            field=models.IntegerField(verbose_name='Holter', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='holter_fa',
            field=models.IntegerField(verbose_name='Rachas de FA o FAP  en Holter', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='holter_fecha',
            field=models.DateField(verbose_name='Fecha de Holter', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='holter_hallazgos',
            field=models.CharField(verbose_name='Hallazgos monitorización FA', null=True, max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='monit_ui',
            field=models.CharField(verbose_name='Hallazgos monitorización UI', null=True, max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='monituifa',
            field=models.IntegerField(verbose_name='DETECCION FA O FAP EN MONITORIZACION UI', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='intervencion',
            name='transf_hemor',
            field=models.IntegerField(verbose_name='Transformación hemorrágica', null=True, blank=True, choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='fecha_muerte',
            field=models.DateField(verbose_name='Fecha de la muerte', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='fop',
            field=models.CharField(verbose_name='Presencia de foramen oval permeable', null=True, max_length=2, choices=[('00', 'No'), ('01', 'Sí')], blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='muertevascular',
            field=models.CharField(verbose_name='Muerte de causa vascular', null=True, max_length=2, choices=[('00', 'No'), ('01', 'Sí')], blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='nihss_3meses',
            field=models.IntegerField(verbose_name='NIHSS 3 meses', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='rankin_3meses',
            field=models.CharField(verbose_name='Escala de Rankin 3 meses', null=True, max_length=2, choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')], blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='rope',
            field=models.FloatField(verbose_name='Escala RoPE para pacientes con FOP', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='toast_3meses',
            field=models.CharField(verbose_name='TOAST 3 meses', null=True, max_length=2, choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')], blank=True),
        ),
    ]
