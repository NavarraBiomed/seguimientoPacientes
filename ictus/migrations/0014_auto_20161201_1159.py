# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0013_auto_20161201_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='NHC',
            new_name='nhc',
        ),
    ]
