# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0028_auto_20161212_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='alcohol',
            field=models.IntegerField(null=True, choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')], blank=True, verbose_name='Alcohol'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tabaquismo',
            field=models.IntegerField(null=True, choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')], blank=True, verbose_name='Tabaco'),
        ),
    ]
