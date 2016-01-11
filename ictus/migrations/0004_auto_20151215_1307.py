# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0003_auto_20151215_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='ait_bcd2',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], verbose_name='ABCD2', blank=True),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='mrs_alta',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], verbose_name='mRS alta'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='nihss_ingreso',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='NIHSS Ingreso'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='tibidtc',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='TIBI/DTC', blank=True),
        ),
    ]
