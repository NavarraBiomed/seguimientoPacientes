# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0002_auto_20151215_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='ecocardio_cardiembolico',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='ecotsa',
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='dosis',
            field=models.PositiveIntegerField(verbose_name='Dosis (mg)', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='medicamento',
            field=models.CharField(choices=[('ANTICOAG_sintrom', 'ANTICOAG Sintrom'), ('ANTICOAG_apixaban', 'ANTICOAG Apixaban'), ('ANTICOAG_rivaroxaban', 'ANTICOAG Rivaroxaban'), ('ANTICOAG_dabigatran', 'ANTICOAG Dabigatran'), ('ANTIAGREG_adiro', 'ANTIAGREG Adiro'), ('ANTIAGREG_clopidogrel', 'ANTIAGREG Clopidogrel'), ('ESTATINAS', 'ESTATINAS'), ('ASPIRINA', 'ASPIRINA')], verbose_name='Medicamento', default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episodio',
            name='mrs_alta',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='mRS alta'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(verbose_name='NIHSS Alta'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='nihss_ingreso',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29)], verbose_name='NIHSS Ingreso'),
        ),
    ]
