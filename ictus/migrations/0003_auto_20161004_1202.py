# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0002_auto_20161003_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='ait_bcd2',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=None, verbose_name='ABCD2'),
        ),
    ]
