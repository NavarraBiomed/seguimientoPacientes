# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0025_auto_20161212_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='antiagregante',
            field=models.IntegerField(null=True, blank=True, verbose_name='Antiagregación previa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='anticoagulante',
            field=models.IntegerField(null=True, blank=True, verbose_name='Anticoagulación previa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='arteriopatia_perif',
            field=models.IntegerField(null=True, blank=True, verbose_name='Arteriopatía periférica previa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancer',
            field=models.IntegerField(null=True, blank=True, verbose_name='Cancer activo', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancerdxposterior',
            field=models.IntegerField(null=True, verbose_name='Cancer diagnosticado tras el ictus', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cardiopatia',
            field=models.IntegerField(null=True, blank=True, verbose_name='Cardiopatía', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dl',
            field=models.IntegerField(null=True, blank=True, verbose_name='Displipemia', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dm',
            field=models.IntegerField(null=True, blank=True, verbose_name='Diabetes mellitus', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='estatinas',
            field=models.IntegerField(null=True, blank=True, verbose_name='Estatina previa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='fa',
            field=models.IntegerField(null=True, blank=True, verbose_name='FAP previa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='hta',
            field=models.IntegerField(null=True, blank=True, verbose_name='Hipertensión', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='ictusaitprevio',
            field=models.IntegerField(null=True, blank=True, verbose_name='Ictus previo', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='acm_hiperdensa',
            field=models.IntegerField(null=True, blank=True, verbose_name='ACM hiperdensa', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ait',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='aitneuroimagen',
            field=models.IntegerField(null=True, blank=True, verbose_name='Neuroimagen AIT', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='aitprevio',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='esus',
            field=models.IntegerField(null=True, blank=True, verbose_name='ESUS', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ev',
            field=models.IntegerField(null=True, blank=True, verbose_name='EV', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ia',
            field=models.IntegerField(null=True, blank=True, verbose_name='Tratamiento Interarterial', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='mimic',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT o Ictus Mimic', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='recanalizacdtc',
            field=models.IntegerField(null=True, blank=True, verbose_name='Recanalización doble transcraneal', choices=[('00', 'No'), ('01', 'Sí')]),
        ),
    ]
