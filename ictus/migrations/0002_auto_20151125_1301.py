# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraccion',
            name='extr_var',
            field=models.CharField(default='', max_length=30),
        ),
    ]
