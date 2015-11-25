# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0007_extraccion_variable_extraccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraccion',
            name='variable_extraccion',
            field=models.CharField(verbose_name='Placeholder variable', max_length=300),
        ),
    ]
