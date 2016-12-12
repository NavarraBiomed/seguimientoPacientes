# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0019_auto_20161201_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basal',
            old_name='inctusaitprevio',
            new_name='ictusaitprevio',
        ),
    ]
