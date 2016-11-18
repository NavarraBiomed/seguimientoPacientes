# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0007_auto_20161117_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='tipo_ictus',
            field=models.CharField(choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')], default=0, verbose_name='Tipo de ictus', max_length=2),
            preserve_default=False,
        ),
    ]
