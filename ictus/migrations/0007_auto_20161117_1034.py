# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0006_auto_20161110_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='ACFA_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='ACFA previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='HTA',
            field=models.CharField(null=True, max_length=2, verbose_name='Hipertensión', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='HTA_tiempo',
            field=models.IntegerField(null=True, verbose_name='Tiempo evolucón HTA', blank=True),
        ),
        migrations.AlterField(
            model_name='basal',
            name='IAM',
            field=models.CharField(null=True, max_length=2, verbose_name='Infarto agudo de miocardio', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='SAOS',
            field=models.CharField(null=True, max_length=2, verbose_name='Síndrome apnea obstructiva sueño', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='TVP',
            field=models.CharField(null=True, max_length=2, verbose_name='Trombosis venosa profunda', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='alcohol',
            field=models.CharField(null=True, max_length=2, verbose_name='Alcohol', blank=True, choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='antecedentes_familiares',
            field=models.BooleanField(verbose_name='Antecedentes familiares', default=False),
        ),
        migrations.AlterField(
            model_name='basal',
            name='antiagregacion_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='Antiagregación previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='anticoagulacion_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='Anticoagulación previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='arritmia_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='Arritmia previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='arteriopatia_perif_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='Arteriopatía periférica previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancer',
            field=models.CharField(null=True, max_length=2, verbose_name='Cancer activo', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancer_tipo',
            field=models.TextField(null=True, max_length=500, verbose_name='Tipo de cancer', blank=True),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cardiopatia_isquemica',
            field=models.CharField(null=True, max_length=2, verbose_name='Cardiopatía isquémica crónica', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='deterioro_cognitivo',
            field=models.CharField(null=True, max_length=2, verbose_name='Deterioro cognitivo', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='diabetes',
            field=models.CharField(null=True, max_length=2, verbose_name='Diabetes mellitus', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dislipemia',
            field=models.CharField(null=True, max_length=2, verbose_name='Displipemia', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='ejercicio',
            field=models.CharField(null=True, max_length=2, verbose_name='Ejercico físico', blank=True, choices=[('00', 'No'), ('01', 'Menos de 3 días/semana'), ('02', 'Más de 3 días/semana'), ('04', 'A diario')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='estatina_previas',
            field=models.CharField(null=True, max_length=2, verbose_name='Estatina previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='fap_previa',
            field=models.CharField(null=True, max_length=2, verbose_name='FAP previa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='ictus_previo',
            field=models.CharField(null=True, max_length=2, verbose_name='Ictus previo', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='migrana',
            field=models.CharField(null=True, max_length=2, verbose_name='Migraña', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='otras_cardiopatias',
            field=models.CharField(null=True, max_length=2, verbose_name='Otras cardiopatías', blank=True, choices=[('00', 'Ninguna'), ('01', 'Miocardiopatía dilatada'), ('02', 'Miocardiopatía hipertrófica'), ('03', 'Miocardiopatía restrictiva'), ('04', 'Cardiopatía valvular'), ('05', 'Cardiopatía isquémica'), ('06', 'Cardiopatía hipertensiva'), ('07', 'Dos o más cardiopatías'), ('08', 'Desconocida'), ('09', 'Otras cardiopatías'), ('10', 'Bloqueo AV marcapasos')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='otras_patologias',
            field=models.TextField(null=True, max_length=500, verbose_name='Otras patologías', blank=True),
        ),
        migrations.AlterField(
            model_name='basal',
            name='rankin',
            field=models.CharField(null=True, max_length=2, verbose_name='Escala de Rankin', blank=True, choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tabaco',
            field=models.CharField(null=True, max_length=2, verbose_name='Tabaco', blank=True, choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tabaco_paquetes_acumulados',
            field=models.IntegerField(null=True, verbose_name='Paquetes/año acumulados', blank=True),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tiempo_diabetes',
            field=models.IntegerField(null=True, verbose_name='Tiempo DM', blank=True),
        ),
        migrations.AlterField(
            model_name='basal',
            name='tipo_diabetes',
            field=models.CharField(null=True, max_length=2, verbose_name='Tipo de DM', blank=True, choices=[('01', 'Tipo 1'), ('02', 'Tipo 2'), ('03', 'Desconocido')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ait',
            field=models.CharField(null=True, max_length=2, verbose_name='AIT', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ait_duracion',
            field=models.TimeField(null=True, verbose_name='Duración AIT', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ait_neuroimagen',
            field=models.CharField(null=True, max_length=2, verbose_name='Neuroimagen AIT', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ev',
            field=models.CharField(null=True, max_length=2, verbose_name='EV', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='fecha_inicio',
            field=models.DateField(null=True, verbose_name='Fecha ictus', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='h_inicio',
            field=models.TimeField(null=True, verbose_name='Hora de inicio', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='hemo_etiologia',
            field=models.CharField(null=True, max_length=2, verbose_name='HEMO etiología', blank=True, choices=[('1', 'Hemorragia primaria-HTA'), ('2', 'Hemorragia secundaria')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='hemo_localizacion',
            field=models.CharField(null=True, max_length=2, verbose_name='HEMO localización', blank=True, choices=[('00', 'No'), ('01', 'Hematoma lobar'), ('02', 'Hematoma subpratentorial profundo'), ('03', 'Hematoma cerebeloso, profundo'), ('04', 'Hematoma troncoencefálico, profundo')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='mrs_alta',
            field=models.IntegerField(null=True, verbose_name='mRS alta', blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='nihss_alta',
            field=models.IntegerField(null=True, verbose_name='NIHSS Alta', blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='nihss_ingreso',
            field=models.IntegerField(null=True, verbose_name='NIHSS Ingreso', blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='oclusion',
            field=models.CharField(null=True, max_length=2, verbose_name='Oclusión', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='oclusion_lugar',
            field=models.CharField(null=True, max_length=2, verbose_name='Lugar de oclusión', blank=True, choices=[('0', 'ACI proximal'), ('1', 'ACI proximal y tandem'), ('2', 'ACI distal terminus'), ('3', 'ACI distal terminus y tandem'), ('4', 'M1'), ('5', 'M2'), ('6', 'BASILAR'), ('7', 'Otros')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='oxfordshire',
            field=models.CharField(null=True, max_length=4, verbose_name='OXFORDSHIRE', blank=True, choices=[('TACI', 'Infartos completos de la circulación anterior'), ('PACI', 'Infartos parciales de la circulación anterior'), ('LACI', 'Infartos lacunares'), ('POCI', 'infartos de la circulación posterior')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='recanalizacion_dtc',
            field=models.CharField(null=True, max_length=2, verbose_name='Recanalización doble transcraneal', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='tipo_ictus',
            field=models.CharField(null=True, max_length=2, verbose_name='Tipo de ictus', blank=True, choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='toast',
            field=models.CharField(null=True, max_length=2, verbose_name='TOAST', blank=True, choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='tratamiento_interarterial',
            field=models.CharField(null=True, max_length=2, verbose_name='Tratamiento Interarterial', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='anatomia_patologica',
            field=models.TextField(null=True, max_length=500, verbose_name='Anatomía patológica', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='aspecto_trombo',
            field=models.TextField(null=True, max_length=500, verbose_name='Aspecto del trombo', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='hora_ext',
            field=models.DateTimeField(null=True, verbose_name='Hora de extracción', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='incidencias',
            field=models.TextField(null=True, max_length=500, verbose_name='Incidencias', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='micro',
            field=models.DateTimeField(null=True, verbose_name='Introcucción de microcateter', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='oktici',
            field=models.CharField(null=True, max_length=2, verbose_name='OKTICI', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='otras',
            field=models.TextField(null=True, max_length=500, verbose_name='Otras', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='peso_trombo',
            field=models.PositiveIntegerField(null=True, verbose_name='Peso (mg)', blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='puncion',
            field=models.DateTimeField(null=True, verbose_name='Punción arterial', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='rescate',
            field=models.DateTimeField(null=True, verbose_name='Hora del rescate', default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='tici',
            field=models.CharField(null=True, max_length=2, verbose_name='TICI', blank=True, choices=[('0', 'No perfusión'), ('1', 'Penetración con mínima perfusión'), ('2', 'Perfusión parcial'), ('2A', 'Relleno parcial'), ('2B', 'Relleno completo'), ('3', 'Perfusión completa')]),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='trombo',
            field=models.CharField(null=True, max_length=2, verbose_name='Extracción de trombo', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='extraccion',
            name='urokinasa',
            field=models.CharField(null=True, max_length=2, verbose_name='Urokinasa', blank=True, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='anticoag_nombre',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='grupo_etnico',
            field=models.CharField(null=True, max_length=2, verbose_name='Grupo étnico', blank=True, choices=[('00', 'Caucásico mediterráneo'), ('01', 'Otro caucásico'), ('02', 'Latinoamericano-caribeño'), ('03', 'Asiático'), ('04', 'Negro o afro-americano'), ('05', 'Otra raza'), ('06', 'No determinado')]),
        ),
    ]
