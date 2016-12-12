# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0014_auto_20161201_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.FloatField(choices=[('00', 'Hombre'), ('01', 'Mujer')], max_length=2, verbose_name='Género'),
        ),
    ]
