# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0008_auto_20151215_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='otras_patologias',
            field=models.TextField(max_length=500, verbose_name='Otras patologías', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='anatomia_patologica',
            field=models.TextField(max_length=500, verbose_name='Anatomía patológica', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='aspecto_trombo',
            field=models.TextField(max_length=500, verbose_name='Aspecto del trombo', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='incidencias',
            field=models.TextField(max_length=500, verbose_name='Incidencias', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='otras',
            field=models.TextField(max_length=500, verbose_name='Otras', blank=True),
        ),
    ]
