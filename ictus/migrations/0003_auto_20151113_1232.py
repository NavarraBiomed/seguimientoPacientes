# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0002_intervencion_anticoag_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='tipo',
            field=models.CharField(max_length=20, default='1'),
        ),
    ]
