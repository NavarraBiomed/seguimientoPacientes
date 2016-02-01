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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ictus_previo', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Ictus previo')),
                ('HTA', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Hipertensión')),
                ('HTA_tiempo', models.IntegerField(verbose_name='Tiempo evolucón HTA')),
                ('diabetes', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Diabetes mellitus')),
                ('tipo_diabetes', models.CharField(choices=[('01', 'Tipo 1'), ('02', 'Tipo 2'), ('03', 'Desconocido')], max_length=2, verbose_name='Tipo de DM')),
                ('tiempo_diabetes', models.IntegerField(verbose_name='Tiempo DM')),
                ('dislipemia', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Displipemia')),
                ('tabaco', models.CharField(choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')], max_length=2, verbose_name='Tabaco')),
                ('tabaco_paquetes_acumulados', models.IntegerField(verbose_name='Paquetes/año acumulados')),
                ('alcohol', models.CharField(choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')], max_length=2, verbose_name='Alcohol')),
                ('ejercicio', models.CharField(choices=[('00', 'No'), ('01', 'Menos de 3 días/semana'), ('02', 'Más de 3 días/semana'), ('04', 'A diario')], max_length=2, verbose_name='Ejercico físico')),
                ('cardiopatia_isquemica', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Cardiopatía isquémica crónica')),
                ('IAM', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Infarto agudo de miocardio')),
                ('otras_cardiopatias', models.CharField(choices=[('00', 'Ninguna'), ('01', 'Miocardiopatía dilatada'), ('02', 'Miocardiopatía hipertrófica'), ('03', 'Miocardiopatía restrictiva'), ('04', 'Cardiopatía valvular'), ('05', 'Cardiopatía isquémica'), ('06', 'Cardiopatía hipertensiva'), ('07', 'Dos o más cardiopatías'), ('08', 'Desconocida'), ('09', 'Otras cardiopatías'), ('10', 'Bloqueo AV marcapasos')], max_length=2, verbose_name='Otras cardiopatías')),
                ('arritmia_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Arritmia previa')),
                ('fap_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='FAP previa')),
                ('ACFA_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='ACFA previa')),
                ('arteriopatia_perif_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Arteriopatía periférica previa')),
                ('TVP', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Trombosis venosa profunda')),
                ('migrana', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Migraña')),
                ('SAOS', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Síndrome apnea obstructiva sueño')),
                ('deterioro_cognitivo', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Deterioro cognitivo')),
                ('cancer', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Cancer activo')),
                ('cancer_tipo', models.TextField(max_length=500, verbose_name='Tipo de cancer')),
                ('anticoagulacion_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Anticoagulación previa')),
                ('antiagregacion_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Antiagregación previa')),
                ('estatina_previas', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Estatina previa')),
                ('otras_patologias', models.TextField(verbose_name='Otras patologías', max_length=500, blank=True)),
                ('antecedentes_familiares', models.BooleanField(verbose_name='Antecedentes familiares')),
                ('rankin', models.CharField(choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')], max_length=2, verbose_name='Escala de Rankin')),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha ictus', default=django.utils.timezone.now)),
                ('h_inicio', models.TimeField(verbose_name='Hora de inicio', default=django.utils.timezone.now)),
                ('hora_inicio_indet', models.BooleanField(default=False, verbose_name='Hora indeterminada')),
                ('tipo_ictus', models.CharField(choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')], max_length=2, verbose_name='Tipo de ictus')),
                ('nihss_ingreso', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='NIHSS Ingreso')),
                ('nihss_alta', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='NIHSS Alta')),
                ('mrs_alta', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], verbose_name='mRS alta')),
                ('toast', models.CharField(choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')], max_length=2, verbose_name='TOAST')),
                ('oxfordshire', models.CharField(choices=[('TACI', 'Infartos completos de la circulación anterior'), ('PACI', 'Infartos parciales de la circulación anterior'), ('LACI', 'Infartos lacunares'), ('POCI', 'infartos de la circulación posterior')], max_length=4, verbose_name='OXFORDSHIRE')),
                ('ait', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='AIT')),
                ('ait_duracion', models.TimeField(verbose_name='Duración AIT', default=django.utils.timezone.now)),
                ('ait_neuroimagen', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Neuroimagen AIT')),
                ('ait_bcd2', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], blank=True, verbose_name='ABCD2')),
                ('hemo_localizacion', models.CharField(choices=[('00', 'No'), ('01', 'Hematoma lobar'), ('02', 'Hematoma subpratentorial profundo'), ('03', 'Hematoma cerebeloso, profundo'), ('04', 'Hematoma troncoencefálico, profundo')], max_length=2, verbose_name='HEMO localización')),
                ('hemo_etiologia', models.CharField(choices=[('1', 'Hemorragia primaria-HTA'), ('2', 'Hemorragia secundaria')], max_length=2, verbose_name='HEMO etiología')),
                ('ev', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='EV')),
                ('recanalizacion_dtc', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Recanalización doble transcraneal')),
                ('oclusion', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Oclusión')),
                ('oclusion_lugar', models.CharField(choices=[('0', 'ACI proximal'), ('1', 'ACI proximal y tandem'), ('2', 'ACI distal terminus'), ('3', 'ACI distal terminus y tandem'), ('4', 'M1'), ('5', 'M2'), ('6', 'BASILAR'), ('7', 'Otros')], max_length=2, verbose_name='Lugar de oclusión')),
                ('tibidtc', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True, verbose_name='TIBI/DTC')),
                ('tratamiento_interarterial', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Tratamiento Interarterial')),
            ],
        ),
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('puncion', models.DateTimeField(verbose_name='Punción arterial', default=django.utils.timezone.now)),
                ('micro', models.DateTimeField(verbose_name='Introcucción de microcateter', default=django.utils.timezone.now)),
                ('rescate', models.DateTimeField(verbose_name='Hora del rescate', default=django.utils.timezone.now)),
                ('urokinasa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Urokinasa')),
                ('recanaliza_ia', models.BooleanField(default=False, verbose_name='Recanalización después de IA')),
                ('tici', models.CharField(choices=[('0', 'No perfusión'), ('1', 'Penetración con mínima perfusión'), ('2', 'Perfusión parcial'), ('2A', 'Relleno parcial'), ('2B', 'Relleno completo'), ('3', 'Perfusión completa')], max_length=2, verbose_name='TICI')),
                ('oktici', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='OKTICI')),
                ('trombo', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], max_length=2, verbose_name='Extracción de trombo')),
                ('hora_ext', models.DateTimeField(verbose_name='Hora de extracción', default=django.utils.timezone.now)),
                ('peso_trombo', models.PositiveIntegerField(verbose_name='Peso (mg)')),
                ('aspecto_trombo', models.TextField(verbose_name='Aspecto del trombo', max_length=500, blank=True)),
                ('anatomia_patologica', models.TextField(verbose_name='Anatomía patológica', max_length=500, blank=True)),
                ('incidencias', models.TextField(verbose_name='Incidencias', max_length=500, blank=True)),
                ('otras', models.TextField(verbose_name='Otras', max_length=500, blank=True)),
                ('episodio', models.ForeignKey(to='ictus.Episodio', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('anticoag_nombre', models.CharField(max_length=300)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('NHC', models.IntegerField(verbose_name='NHC')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del paciente ')),
                ('iniciales', models.CharField(max_length=6, verbose_name='Iniciales del paciente')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('00', 'Hombre'), ('01', 'Mujer')], max_length=2, verbose_name='Género')),
                ('grupo_etnico', models.CharField(choices=[('00', 'Caucásico mediterráneo'), ('01', 'Otro caucásico'), ('02', 'Latinoamericano-caribeño'), ('03', 'Asiático'), ('04', 'Negro o afro-americano'), ('05', 'Otra raza'), ('06', 'No determinado')], max_length=2, verbose_name='Grupo étnico')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('variable_seguimiento', models.CharField(max_length=30, verbose_name='Placeholder variable seg')),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('medicamento', models.CharField(choices=[('ANTICOAG_sintrom', 'ANTICOAG Sintrom'), ('ANTICOAG_apixaban', 'ANTICOAG Apixaban'), ('ANTICOAG_rivaroxaban', 'ANTICOAG Rivaroxaban'), ('ANTICOAG_dabigatran', 'ANTICOAG Dabigatran'), ('ANTIAGREG_adiro', 'ANTIAGREG Adiro'), ('ANTIAGREG_clopidogrel', 'ANTIAGREG Clopidogrel'), ('ESTATINAS', 'ESTATINAS'), ('ASPIRINA', 'ASPIRINA')], max_length=30, verbose_name='Medicamento')),
                ('dosis', models.PositiveIntegerField(verbose_name='Dosis (mg)')),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
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
