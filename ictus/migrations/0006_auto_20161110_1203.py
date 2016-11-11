# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0005_auto_20161004_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha ictus'),
        ),
    ]
