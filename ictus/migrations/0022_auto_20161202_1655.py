# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0021_auto_20161202_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='idmuestra',
            field=models.CharField(verbose_name='ID', default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episodio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
        ),
    ]
