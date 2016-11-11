# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0004_auto_20161004_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='tibidtc',
            field=models.IntegerField(blank=True, verbose_name='TIBI/DTC', null=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
