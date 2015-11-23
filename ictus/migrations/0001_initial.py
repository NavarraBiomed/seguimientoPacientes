# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('rank_basal', models.IntegerField(verbose_name='')),
                ('deterioro_fluct', models.IntegerField(verbose_name='')),
                ('transf_hemor', models.IntegerField(verbose_name='')),
                ('hta', models.IntegerField(verbose_name='')),
                ('dm', models.IntegerField(verbose_name='')),
                ('dl', models.IntegerField(verbose_name='')),
                ('fa', models.IntegerField(verbose_name='')),
                ('cardiopatia', models.IntegerField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('h_inicio', models.DateTimeField()),
                ('tipo', models.CharField(max_length=2, choices=[('00', 'Tipo 1'), ('01', 'Tipo 2')])),
            ],
        ),
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('NHC', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=2, choices=[('00', 'Hombre'), ('01', 'Mujer')])),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='extraccion',
            name='Intervencion',
            field=models.ForeignKey(to='ictus.Intervencion'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='paciente',
            field=models.ForeignKey(to='ictus.Paciente'),
        ),
        migrations.AddField(
            model_name='basal',
            name='episodio',
            field=models.ForeignKey(to='ictus.Episodio'),
        ),
    ]
