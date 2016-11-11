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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ictus_previo', models.CharField(verbose_name='Ictus previo', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('HTA', models.CharField(verbose_name='Hipertensión', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('HTA_tiempo', models.IntegerField(verbose_name='Tiempo evolucón HTA')),
                ('diabetes', models.CharField(verbose_name='Diabetes mellitus', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('tipo_diabetes', models.CharField(verbose_name='Tipo de DM', max_length=2, choices=[('01', 'Tipo 1'), ('02', 'Tipo 2'), ('03', 'Desconocido')])),
                ('tiempo_diabetes', models.IntegerField(verbose_name='Tiempo DM')),
                ('dislipemia', models.CharField(verbose_name='Displipemia', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('tabaco', models.CharField(verbose_name='Tabaco', max_length=2, choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')])),
                ('tabaco_paquetes_acumulados', models.IntegerField(verbose_name='Paquetes/año acumulados')),
                ('alcohol', models.CharField(verbose_name='Alcohol', max_length=2, choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')])),
                ('ejercicio', models.CharField(verbose_name='Ejercico físico', max_length=2, choices=[('00', 'No'), ('01', 'Menos de 3 días/semana'), ('02', 'Más de 3 días/semana'), ('04', 'A diario')])),
                ('cardiopatia_isquemica', models.CharField(verbose_name='Cardiopatía isquémica crónica', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('IAM', models.CharField(verbose_name='Infarto agudo de miocardio', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('otras_cardiopatias', models.CharField(verbose_name='Otras cardiopatías', max_length=2, choices=[('00', 'Ninguna'), ('01', 'Miocardiopatía dilatada'), ('02', 'Miocardiopatía hipertrófica'), ('03', 'Miocardiopatía restrictiva'), ('04', 'Cardiopatía valvular'), ('05', 'Cardiopatía isquémica'), ('06', 'Cardiopatía hipertensiva'), ('07', 'Dos o más cardiopatías'), ('08', 'Desconocida'), ('09', 'Otras cardiopatías'), ('10', 'Bloqueo AV marcapasos')])),
                ('arritmia_previa', models.CharField(verbose_name='Arritmia previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('fap_previa', models.CharField(verbose_name='FAP previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('ACFA_previa', models.CharField(verbose_name='ACFA previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('arteriopatia_perif_previa', models.CharField(verbose_name='Arteriopatía periférica previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('TVP', models.CharField(verbose_name='Trombosis venosa profunda', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('migrana', models.CharField(verbose_name='Migraña', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('SAOS', models.CharField(verbose_name='Síndrome apnea obstructiva sueño', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('deterioro_cognitivo', models.CharField(verbose_name='Deterioro cognitivo', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('cancer', models.CharField(verbose_name='Cancer activo', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('cancer_tipo', models.TextField(verbose_name='Tipo de cancer', max_length=500)),
                ('anticoagulacion_previa', models.CharField(verbose_name='Anticoagulación previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('antiagregacion_previa', models.CharField(verbose_name='Antiagregación previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('estatina_previas', models.CharField(verbose_name='Estatina previa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('otras_patologias', models.TextField(verbose_name='Otras patologías', max_length=500, blank=True)),
                ('antecedentes_familiares', models.BooleanField(verbose_name='Antecedentes familiares')),
                ('rankin', models.CharField(verbose_name='Escala de Rankin', max_length=2, choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')])),
            ],
            options={
                'verbose_name_plural': 'Basales',
            },
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha ictus', default=django.utils.timezone.now)),
                ('h_inicio', models.TimeField(verbose_name='Hora de inicio', default=django.utils.timezone.now)),
                ('hora_inicio_indet', models.BooleanField(verbose_name='Hora indeterminada', default=False)),
                ('tipo_ictus', models.CharField(verbose_name='Tipo de ictus', max_length=2, choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')])),
                ('nihss_ingreso', models.IntegerField(verbose_name='NIHSS Ingreso', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)])),
                ('nihss_alta', models.IntegerField(verbose_name='NIHSS Alta', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)])),
                ('mrs_alta', models.IntegerField(verbose_name='mRS alta', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('toast', models.CharField(verbose_name='TOAST', max_length=2, choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')])),
                ('oxfordshire', models.CharField(verbose_name='OXFORDSHIRE', max_length=4, choices=[('TACI', 'Infartos completos de la circulación anterior'), ('PACI', 'Infartos parciales de la circulación anterior'), ('LACI', 'Infartos lacunares'), ('POCI', 'infartos de la circulación posterior')])),
                ('ait', models.CharField(verbose_name='AIT', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('ait_duracion', models.TimeField(verbose_name='Duración AIT', default=django.utils.timezone.now)),
                ('ait_neuroimagen', models.CharField(verbose_name='Neuroimagen AIT', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('ait_bcd2', models.IntegerField(verbose_name='ABCD2', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], blank=True)),
                ('hemo_localizacion', models.CharField(verbose_name='HEMO localización', max_length=2, choices=[('00', 'No'), ('01', 'Hematoma lobar'), ('02', 'Hematoma subpratentorial profundo'), ('03', 'Hematoma cerebeloso, profundo'), ('04', 'Hematoma troncoencefálico, profundo')])),
                ('hemo_etiologia', models.CharField(verbose_name='HEMO etiología', max_length=2, choices=[('1', 'Hemorragia primaria-HTA'), ('2', 'Hemorragia secundaria')])),
                ('ev', models.CharField(verbose_name='EV', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('recanalizacion_dtc', models.CharField(verbose_name='Recanalización doble transcraneal', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('oclusion', models.CharField(verbose_name='Oclusión', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('oclusion_lugar', models.CharField(verbose_name='Lugar de oclusión', max_length=2, choices=[('0', 'ACI proximal'), ('1', 'ACI proximal y tandem'), ('2', 'ACI distal terminus'), ('3', 'ACI distal terminus y tandem'), ('4', 'M1'), ('5', 'M2'), ('6', 'BASILAR'), ('7', 'Otros')])),
                ('tibidtc', models.IntegerField(verbose_name='TIBI/DTC', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True)),
                ('tratamiento_interarterial', models.CharField(verbose_name='Tratamiento Interarterial', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
            ],
        ),
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('puncion', models.DateTimeField(verbose_name='Punción arterial', default=django.utils.timezone.now)),
                ('micro', models.DateTimeField(verbose_name='Introcucción de microcateter', default=django.utils.timezone.now)),
                ('rescate', models.DateTimeField(verbose_name='Hora del rescate', default=django.utils.timezone.now)),
                ('urokinasa', models.CharField(verbose_name='Urokinasa', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('recanaliza_ia', models.BooleanField(verbose_name='Recanalización después de IA', default=False)),
                ('tici', models.CharField(verbose_name='TICI', max_length=2, choices=[('0', 'No perfusión'), ('1', 'Penetración con mínima perfusión'), ('2', 'Perfusión parcial'), ('2A', 'Relleno parcial'), ('2B', 'Relleno completo'), ('3', 'Perfusión completa')])),
                ('oktici', models.CharField(verbose_name='OKTICI', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('trombo', models.CharField(verbose_name='Extracción de trombo', max_length=2, choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')])),
                ('hora_ext', models.DateTimeField(verbose_name='Hora de extracción', default=django.utils.timezone.now)),
                ('peso_trombo', models.PositiveIntegerField(verbose_name='Peso (mg)')),
                ('aspecto_trombo', models.TextField(verbose_name='Aspecto del trombo', max_length=500, blank=True)),
                ('anatomia_patologica', models.TextField(verbose_name='Anatomía patológica', max_length=500, blank=True)),
                ('incidencias', models.TextField(verbose_name='Incidencias', max_length=500, blank=True)),
                ('otras', models.TextField(verbose_name='Otras', max_length=500, blank=True)),
                ('episodio', models.ForeignKey(to='ictus.Episodio', null=True)),
            ],
            options={
                'verbose_name_plural': 'Extracciones',
            },
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('anticoag_nombre', models.CharField(max_length=300)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
            options={
                'verbose_name_plural': 'Intervenciones',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('NHC', models.IntegerField(verbose_name='NHC')),
                ('nombre', models.CharField(verbose_name='Nombre del paciente ', max_length=30)),
                ('iniciales', models.CharField(verbose_name='Iniciales del paciente', max_length=6)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(verbose_name='Género', max_length=2, choices=[('00', 'Hombre'), ('01', 'Mujer')])),
                ('grupo_etnico', models.CharField(verbose_name='Grupo étnico', max_length=2, choices=[('00', 'Caucásico mediterráneo'), ('01', 'Otro caucásico'), ('02', 'Latinoamericano-caribeño'), ('03', 'Asiático'), ('04', 'Negro o afro-americano'), ('05', 'Otra raza'), ('06', 'No determinado')])),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('variable_seguimiento', models.CharField(verbose_name='Placeholder variable seg', max_length=30)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('medicamento', models.CharField(verbose_name='Medicamento', max_length=30, choices=[('ANTICOAG_sintrom', 'ANTICOAG Sintrom'), ('ANTICOAG_apixaban', 'ANTICOAG Apixaban'), ('ANTICOAG_rivaroxaban', 'ANTICOAG Rivaroxaban'), ('ANTICOAG_dabigatran', 'ANTICOAG Dabigatran'), ('ANTIAGREG_adiro', 'ANTIAGREG Adiro'), ('ANTIAGREG_clopidogrel', 'ANTIAGREG Clopidogrel'), ('ESTATINAS', 'ESTATINAS'), ('ASPIRINA', 'ASPIRINA')])),
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
