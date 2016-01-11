# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0006_auto_20151215_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(verbose_name='NIHSS Alta', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='oxfordshire',
            field=models.CharField(verbose_name='OXFORDSHIRE', choices=[('TACI', 'Infartos completos de la circulación anterior'), ('PACI', 'Infartos parciales de la circulación anterior'), ('LACI', 'Infartos lacunares'), ('POCI', 'infartos de la circulación posterior')], max_length=4),
        ),
    ]
