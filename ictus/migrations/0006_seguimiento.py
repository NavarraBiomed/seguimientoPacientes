# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0005_auto_20151124_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('variable_seguimiento', models.IntegerField(verbose_name='Placeholder variable')),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
    ]
