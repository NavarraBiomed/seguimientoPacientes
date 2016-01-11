# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='mrs_alta',
            field=models.IntegerField(max_length=2, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='mRS alta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(max_length=2, default=0, verbose_name='NIHSS Alta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodio',
            name='nihss_ingreso',
            field=models.IntegerField(max_length=2, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29)], default=0, verbose_name='NIHSS Ingreso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episodio',
            name='tipo_ictus',
            field=models.CharField(choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')], max_length=2, verbose_name='Tipo de ictus'),
        ),
    ]
