# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0009_auto_20161117_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='comentarios',
            field=models.TextField(null=True, blank=True, verbose_name='Comentarios', max_length=1024),
        ),
        migrations.AddField(
            model_name='episodio',
            name='completo',
            field=models.BooleanField(default=False, verbose_name='Completo'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='lesion',
            field=models.BooleanField(default=False, verbose_name='Lesión'),
        ),
    ]
