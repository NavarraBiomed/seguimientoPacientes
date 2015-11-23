# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervencion',
            name='anticoag_nombre',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
