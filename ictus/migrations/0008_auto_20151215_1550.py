# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0007_auto_20151215_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraccion',
            name='Intervencion',
        ),
        migrations.RemoveField(
            model_name='extraccion',
            name='extr_var',
        ),
        migrations.AddField(
            model_name='extraccion',
            name='anatomia_patologica',
            field=models.TextField(verbose_name='Anatomía patológica', default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='aspecto_trombo',
            field=models.TextField(verbose_name='Aspecto del trombo', default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='episodio',
            field=models.ForeignKey(null=True, to='ictus.Episodio'),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='hora_ext',
            field=models.DateTimeField(verbose_name='Hora de extracción', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='incidencias',
            field=models.TextField(verbose_name='Incidencias', default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='micro',
            field=models.DateTimeField(verbose_name='Introcucción de microcateter', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='oktici',
            field=models.CharField(verbose_name='OKTICI', default=0, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='otras',
            field=models.TextField(verbose_name='Otras', default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='peso_trombo',
            field=models.PositiveIntegerField(verbose_name='Peso (mg)', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='puncion',
            field=models.DateTimeField(verbose_name='Punción arterial', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='recanaliza_ia',
            field=models.BooleanField(default=False, verbose_name='Recanalización después de IA'),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='rescate',
            field=models.DateTimeField(verbose_name='Hora del rescate', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='extraccion',
            name='tici',
            field=models.CharField(verbose_name='TICI', default=0, choices=[('0', 'No perfusión'), ('1', 'Penetración con mínima perfusión'), ('2', 'Perfusión parcial'), ('2A', 'Relleno parcial'), ('2B', 'Relleno completo'), ('3', 'Perfusión completa')], max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='trombo',
            field=models.CharField(verbose_name='Extracción de trombo', default=0, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraccion',
            name='urokinasa',
            field=models.CharField(verbose_name='Urokinasa', default=0, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancer_tipo',
            field=models.TextField(verbose_name='Tipo de cancer', max_length=500),
        ),
        migrations.AlterField(
            model_name='basal',
            name='otras_patologias',
            field=models.TextField(verbose_name='Otras patologías', max_length=500),
        ),
    ]
