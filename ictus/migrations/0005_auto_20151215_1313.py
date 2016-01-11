# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0004_auto_20151215_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')], verbose_name='NIHSS Alta'),
        ),
    ]
