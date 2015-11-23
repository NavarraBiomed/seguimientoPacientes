# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0003_auto_20151113_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='tipo',
            field=models.CharField(max_length=2, choices=[('00', 'Tipo 1'), ('01', 'Tipo 2')]),
        ),
    ]
