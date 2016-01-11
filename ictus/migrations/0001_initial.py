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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ictus_previo', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Ictus previo', max_length=2)),
                ('HTA', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Hipertensión', max_length=2)),
                ('HTA_tiempo', models.IntegerField(verbose_name='Tiempo evolucón HTA')),
                ('diabetes', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Diabetes mellitus', max_length=2)),
                ('tipo_diabetes', models.CharField(choices=[('01', 'Tipo 1'), ('02', 'Tipo 2'), ('03', 'Desconocido')], verbose_name='Tipo de DM', max_length=2)),
                ('tiempo_diabetes', models.IntegerField(verbose_name='Tiempo DM')),
                ('dislipemia', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Displipemia', max_length=2)),
                ('tabaco', models.CharField(choices=[('00', 'No fumador'), ('01', 'Exfumador'), ('02', 'Fumador pasivo'), ('03', 'Fumador actual'), ('04', 'Desconocido')], verbose_name='Tabaco', max_length=2)),
                ('tabaco_paquetes_acumulados', models.IntegerField(verbose_name='Paquetes/año acumulados')),
                ('alcohol', models.CharField(choices=[('00', 'No'), ('01', 'A diario'), ('02', 'Ocasionalmente'), ('03', 'Exhabito enólico')], verbose_name='Alcohol', max_length=2)),
                ('ejercicio', models.CharField(choices=[('00', 'No'), ('01', 'Menos de 3 días/semana'), ('02', 'Más de 3 días/semana'), ('04', 'A diario')], verbose_name='Ejercico físico', max_length=2)),
                ('cardiopatia_isquemica', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Cardiopatía isquémica crónica', max_length=2)),
                ('IAM', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Infarto agudo de miocardio', max_length=2)),
                ('otras_cardiopatias', models.CharField(choices=[('00', 'Ninguna'), ('01', 'Miocardiopatía dilatada'), ('02', 'Miocardiopatía hipertrófica'), ('03', 'Miocardiopatía restrictiva'), ('04', 'Cardiopatía valvular'), ('05', 'Cardiopatía isquémica'), ('06', 'Cardiopatía hipertensiva'), ('07', 'Dos o más cardiopatías'), ('08', 'Desconocida'), ('09', 'Otras cardiopatías'), ('10', 'Bloqueo AV marcapasos')], verbose_name='Otras cardiopatías', max_length=2)),
                ('arritmia_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Arritmia previa', max_length=2)),
                ('fap_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='FAP previa', max_length=2)),
                ('ACFA_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='ACFA previa', max_length=2)),
                ('arteriopatia_perif_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Arteriopatía periférica previa', max_length=2)),
                ('TVP', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Trombosis venosa profunda', max_length=2)),
                ('migrana', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Migraña', max_length=2)),
                ('SAOS', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Síndrome apnea obstructiva sueño', max_length=2)),
                ('deterioro_cognitivo', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Deterioro cognitivo', max_length=2)),
                ('cancer', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Cancer activo', max_length=2)),
                ('cancer_tipo', models.CharField(verbose_name='Tipo de cancer', max_length=50)),
                ('anticoagulacion_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Anticoagulación previa', max_length=2)),
                ('antiagregacion_previa', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Antiagregación previa', max_length=2)),
                ('estatina_previas', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Estatina previa', max_length=2)),
                ('otras_patologias', models.CharField(verbose_name='Otras patologías', max_length=100)),
                ('antecedentes_familiares', models.BooleanField(verbose_name='Antecedentes familiares')),
                ('rankin', models.CharField(choices=[('0', 'Sin síntomas'), ('1', 'Sin incapacidad importante'), ('2', 'Incapacidad leve'), ('3', 'Incapacidad moderada'), ('4', 'Incapacidad moderadamente grave'), ('5', 'Incapacidad grave'), ('6', 'Muerte')], verbose_name='Escala de Rankin', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha ictus')),
                ('h_inicio', models.TimeField(default=django.utils.timezone.now, verbose_name='Hora de inicio')),
                ('hora_inicio_indet', models.BooleanField(default=False, verbose_name='Hora indeterminada')),
                ('tipo_ictus', models.CharField(choices=[('00', 'Isquémico'), ('01', 'Hemorrágico'), ('02', 'Isquemia transitoria'), ('03', 'Mimic')], verbose_name=' Tipo de ictus', max_length=2)),
                ('toast', models.CharField(choices=[('1', 'Aterotrombótico'), ('2', 'Cardioembólico'), ('3', 'Lacunar'), ('4', 'De otra etiología determinada/causa infrecuente'), ('5', 'Indeterminado, >2 causas'), ('6', 'Indeterminado, tras estudio completo'), ('7', 'Indeterminado, estudio incompleto')], verbose_name='TOAST', max_length=2)),
                ('oxfordshire', models.CharField(choices=[('TACI', 'Infartos completos de la circulación anterior'), ('PACI', 'Infartos parciales de la circulación anterior'), ('LACI', 'Infartos lacunares'), ('POCI', 'infartos de la circulación posterior')], verbose_name='OXFORDSHIRE', max_length=2)),
                ('ait', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='AIT', max_length=2)),
                ('ait_duracion', models.TimeField(default=django.utils.timezone.now, verbose_name='Duración AIT')),
                ('ait_neuroimagen', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Neuroimagen AIT', max_length=2)),
                ('ait_bcd2', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], verbose_name='ABCD2')),
                ('hemo_localizacion', models.CharField(choices=[('00', 'No'), ('01', 'Hematoma lobar'), ('02', 'Hematoma subpratentorial profundo'), ('03', 'Hematoma cerebeloso, profundo'), ('04', 'Hematoma troncoencefálico, profundo')], verbose_name='HEMO localización', max_length=2)),
                ('hemo_etiologia', models.CharField(choices=[('1', 'Hemorragia primaria-HTA'), ('2', 'Hemorragia secundaria')], verbose_name='HEMO etiología', max_length=2)),
                ('ev', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='EV', max_length=2)),
                ('recanalizacion_dtc', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Recanalización doble transcraneal', max_length=2)),
                ('oclusion', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Oclusión', max_length=2)),
                ('oclusion_lugar', models.CharField(choices=[('0', 'ACI proximal'), ('1', 'ACI proximal y tandem'), ('2', 'ACI distal terminus'), ('3', 'ACI distal terminus y tandem'), ('4', 'M1'), ('5', 'M2'), ('6', 'BASILAR'), ('7', 'Otros')], verbose_name='Lugar de oclusión', max_length=2)),
                ('tibidtc', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='TIBI/DTC')),
                ('tratamiento_interarterial', models.CharField(choices=[('00', 'No'), ('01', 'Sí'), ('02', 'Indeterminado')], verbose_name='Tratamiento Interarterial', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extr_var', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anticoag_nombre', models.CharField(max_length=300)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NHC', models.IntegerField(verbose_name='NHC')),
                ('nombre', models.CharField(verbose_name='Nombre del paciente ', max_length=30)),
                ('iniciales', models.CharField(verbose_name='Iniciales del paciente', max_length=6)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('00', 'Hombre'), ('01', 'Mujer')], verbose_name='Género', max_length=2)),
                ('grupo_etnico', models.CharField(choices=[('00', 'Caucásico mediterráneo'), ('01', 'Otro caucásico'), ('02', 'Latinoamericano-caribeño'), ('03', 'Asiático'), ('04', 'Negro o afro-americano'), ('05', 'Otra raza'), ('06', 'No determinado')], verbose_name='Grupo étnico', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_seguimiento', models.CharField(verbose_name='Placeholder variable seg', max_length=30)),
                ('episodio', models.ForeignKey(to='ictus.Episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
