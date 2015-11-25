# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0009_auto_20151125_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervencion',
            name='anticoag_nombre',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='variable_seguimiento',
            field=models.CharField(verbose_name='Placeholder variable seg', max_length=30),
        ),
    ]
