# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0003_auto_20161004_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='ait_bcd2',
            field=models.IntegerField(blank=True, verbose_name='ABCD2', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], null=True),
        ),
    ]
