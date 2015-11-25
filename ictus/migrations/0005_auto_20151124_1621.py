# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0004_auto_20151113_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ecocardio_cardiembolico', models.IntegerField(verbose_name='Cardioembolicas')),
                ('ecotsa', models.CharField(max_length=3000)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.AlterField(
            model_name='basal',
            name='cardiopatia',
            field=models.IntegerField(verbose_name='Cardiopatia'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='deterioro_fluct',
            field=models.IntegerField(verbose_name='Deteriorio'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dl',
            field=models.IntegerField(verbose_name='Dislipemia'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dm',
            field=models.IntegerField(verbose_name='Diabetes mellitus'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='fa',
            field=models.IntegerField(verbose_name='Fibrilación auricular'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='hta',
            field=models.IntegerField(verbose_name='HTA'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='rank_basal',
            field=models.IntegerField(verbose_name='Ranking Basal'),
        ),
        migrations.AlterField(
            model_name='basal',
            name='transf_hemor',
            field=models.IntegerField(verbose_name='Transformación hemorrágica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
