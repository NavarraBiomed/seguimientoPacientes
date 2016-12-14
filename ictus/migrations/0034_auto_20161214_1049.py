# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0033_auto_20161212_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='oxfordshire',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Infartos completos de la circulación anterior'), (1, 'Infartos parciales de la circulación anterior'), (2, 'Infartos lacunares'), (3, 'infartos de la circulación posterior')], verbose_name='OXFORDSHIRE'),
        ),
    ]
