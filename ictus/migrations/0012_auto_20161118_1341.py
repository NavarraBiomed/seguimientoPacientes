# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0011_auto_20161118_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguimiento',
            name='causa_muerte',
            field=models.TextField(max_length=3000, verbose_name='Causa de la muerte', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='nihss_3meses',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='NIHSS 3 meses', null=True),
        ),
    ]
