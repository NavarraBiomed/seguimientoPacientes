# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rank_basal', models.IntegerField(verbose_name='Ranking Basal')),
                ('deterioro_fluct', models.IntegerField(verbose_name='Deteriorio')),
                ('transf_hemor', models.IntegerField(verbose_name='Transformación hemorrágica')),
                ('hta', models.IntegerField(verbose_name='HTA')),
                ('dm', models.IntegerField(verbose_name='Diabetes mellitus')),
                ('dl', models.IntegerField(verbose_name='Dislipemia')),
                ('fa', models.IntegerField(verbose_name='Fibrilación auricular')),
                ('cardiopatia', models.IntegerField(verbose_name='Cardiopatia')),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('h_inicio', models.DateTimeField()),
                ('tipo', models.CharField(max_length=2, choices=[('00', 'Tipo 1'), ('01', 'Tipo 2')])),
            ],
        ),
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('extr_var', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('anticoag_nombre', models.CharField(max_length=300)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('NHC', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=2, choices=[('00', 'Hombre'), ('01', 'Mujer')])),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('variable_seguimiento', models.CharField(verbose_name='Placeholder variable seg', max_length=30)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ecocardio_cardiembolico', models.IntegerField(verbose_name='Cardioembolicas')),
                ('ecotsa', models.CharField(max_length=3000)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
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
