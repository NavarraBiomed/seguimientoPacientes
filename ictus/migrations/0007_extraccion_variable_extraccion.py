# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0006_seguimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraccion',
            name='variable_extraccion',
            field=models.IntegerField(default='', verbose_name='Placeholder variable'),
            preserve_default=False,
        ),
    ]
