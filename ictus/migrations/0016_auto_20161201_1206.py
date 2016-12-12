# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0015_auto_20161201_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, verbose_name='Fecha de nacimiento', null=True),
        ),
    ]
