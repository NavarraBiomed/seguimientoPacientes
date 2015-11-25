# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0008_auto_20151125_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraccion',
            name='variable_extraccion',
            field=models.IntegerField(verbose_name='Placeholder variable'),
        ),
    ]
