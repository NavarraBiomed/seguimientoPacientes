# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0023_auto_20161212_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intraarterial',
            options={'verbose_name_plural': 'Intraarterial'},
        ),
        migrations.AlterField(
            model_name='basal',
            name='toast_ictusprev',
            field=models.IntegerField(choices=[(0, 'Aterotrombótico'), (1, 'Cardioembólico'), (2, 'Lacunar'), (3, 'De otra etiología determinada/causa infrecuente'), (4, 'Indeterminado, >2 causas'), (5, 'Indeterminado, tras estudio completo'), (6, 'Indeterminado, estudio incompleto')], null=True, blank=True, verbose_name='TOAST ictus previo'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='clasifsen',
            field=models.IntegerField(choices=[(0, 'Aterotrombótico'), (1, 'Cardioembólico'), (2, 'Lacunar'), (3, 'De otra etiología determinada/causa infrecuente'), (4, 'Indeterminado, >2 causas'), (5, 'Indeterminado, tras estudio completo'), (6, 'Indeterminado, estudio incompleto')], null=True, blank=True, verbose_name='SEN'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='toast',
            field=models.IntegerField(choices=[(0, 'Aterotrombótico'), (1, 'Cardioembólico'), (2, 'Lacunar'), (3, 'De otra etiología determinada/causa infrecuente'), (4, 'Indeterminado, >2 causas'), (5, 'Indeterminado, tras estudio completo'), (6, 'Indeterminado, estudio incompleto')], null=True, blank=True, verbose_name='TOAST'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='recurrenciatoast',
            field=models.IntegerField(choices=[(0, 'Aterotrombótico'), (1, 'Cardioembólico'), (2, 'Lacunar'), (3, 'De otra etiología determinada/causa infrecuente'), (4, 'Indeterminado, >2 causas'), (5, 'Indeterminado, tras estudio completo'), (6, 'Indeterminado, estudio incompleto')], null=True, blank=True, verbose_name='TOAST recurrencia'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='toast3m',
            field=models.IntegerField(choices=[(0, 'Aterotrombótico'), (1, 'Cardioembólico'), (2, 'Lacunar'), (3, 'De otra etiología determinada/causa infrecuente'), (4, 'Indeterminado, >2 causas'), (5, 'Indeterminado, tras estudio completo'), (6, 'Indeterminado, estudio incompleto')], null=True, blank=True, verbose_name='TOAST 3 meses'),
        ),
    ]
