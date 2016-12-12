# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0032_auto_20161212_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='episodio',
        ),
        migrations.DeleteModel(
            name='Tratamiento',
        ),
    ]
