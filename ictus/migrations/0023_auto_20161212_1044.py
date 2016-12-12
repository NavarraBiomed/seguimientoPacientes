# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0022_auto_20161202_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='aitdurac',
            field=models.IntegerField(blank=True, verbose_name='Duración AIT (min)', null=True),
        ),
    ]
