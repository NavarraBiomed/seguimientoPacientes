# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0030_auto_20161212_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervencion',
            old_name='reacanalizacdtc',
            new_name='recanalizacdtc',
        ),
    ]
