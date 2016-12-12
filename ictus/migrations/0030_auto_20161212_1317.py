# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0029_auto_20161212_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='alcohol',
            field=models.IntegerField(blank=True, verbose_name='Alcohol', null=True, choices=[(0, 'No'), (1, 'A diario'), (2, 'Ocasionalmente'), (3, 'Exhabito enólico')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tabaquismo',
            field=models.IntegerField(blank=True, verbose_name='Tabaco', null=True, choices=[(0, 'No fumador'), (1, 'Exfumador'), (2, 'Fumador pasivo'), (3, 'Fumador actual'), (4, 'Desconocido')]),
        ),
    ]
