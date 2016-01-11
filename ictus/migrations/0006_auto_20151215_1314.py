# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0005_auto_20151215_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(verbose_name='NIHSS Alta'),
        ),
    ]
