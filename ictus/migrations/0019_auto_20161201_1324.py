# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0018_auto_20161201_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basal',
            old_name='arteriopatia_perif_previa',
            new_name='arteriopatia_perif',
        ),
        migrations.RenameField(
            model_name='basal',
            old_name='fap_previa',
            new_name='fa',
        ),
        migrations.RenameField(
            model_name='basal',
            old_name='ictus_previo',
            new_name='inctusaitprevio',
        ),
        migrations.RenameField(
            model_name='basal',
            old_name='tabaco',
            new_name='tabaquismo',
        ),
        migrations.RenameField(
            model_name='basal',
            old_name='toast_ictus_previo',
            new_name='toast_ictusprev',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='ait_bcd2',
            new_name='abcd2',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='ait_bcd3',
            new_name='abcd3',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='ait_duracion',
            new_name='aitdurac',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='ait_neuroimagen',
            new_name='aitneuroimagen',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='ait_previo',
            new_name='aitprevio',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='clasif_sen',
            new_name='clasifsen',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='fecha_inicio',
            new_name='fechaictus',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='hora_inicio_indet',
            new_name='h_inicioindet',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='tratamiento_interarterial',
            new_name='ia',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='nihss_alta',
            new_name='nihssalta',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='nihss_ingreso',
            new_name='nihssb',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='mrs_alta',
            new_name='rankinalta',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='recanalizacion_dtc',
            new_name='recanalizacdtc',
        ),
        migrations.AlterField(
            model_name='episodio',
            name='paciente',
            field=models.ForeignKey(to='ictus.Paciente', related_name='episodios'),
        ),
    ]
