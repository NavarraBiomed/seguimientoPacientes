# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0026_auto_20161212_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basal',
            name='antiagregante',
            field=models.IntegerField(null=True, blank=True, verbose_name='Antiagregación previa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='anticoagulante',
            field=models.IntegerField(null=True, blank=True, verbose_name='Anticoagulación previa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='arteriopatia_perif',
            field=models.IntegerField(null=True, blank=True, verbose_name='Arteriopatía periférica previa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancer',
            field=models.IntegerField(null=True, blank=True, verbose_name='Cancer activo', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cancerdxposterior',
            field=models.IntegerField(null=True, verbose_name='Cancer diagnosticado tras el ictus', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='cardiopatia',
            field=models.IntegerField(null=True, blank=True, verbose_name='Cardiopatía', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dl',
            field=models.IntegerField(null=True, blank=True, verbose_name='Displipemia', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='dm',
            field=models.IntegerField(null=True, blank=True, verbose_name='Diabetes mellitus', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='estatinas',
            field=models.IntegerField(null=True, blank=True, verbose_name='Estatina previa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='fa',
            field=models.IntegerField(null=True, blank=True, verbose_name='FAP previa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='hta',
            field=models.IntegerField(null=True, blank=True, verbose_name='Hipertensión', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='basal',
            name='ictusaitprevio',
            field=models.IntegerField(null=True, blank=True, verbose_name='Ictus previo', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='abcd3',
            field=models.IntegerField(null=True, blank=True, verbose_name='ABCD3', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='acm_hiperdensa',
            field=models.IntegerField(null=True, blank=True, verbose_name='ACM hiperdensa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ait',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='aitneuroimagen',
            field=models.IntegerField(null=True, blank=True, verbose_name='Neuroimagen AIT', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='aitprevio',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='esus',
            field=models.IntegerField(null=True, blank=True, verbose_name='ESUS', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ev',
            field=models.IntegerField(null=True, blank=True, verbose_name='EV', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='ia',
            field=models.IntegerField(null=True, blank=True, verbose_name='Tratamiento Interarterial', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='mimic',
            field=models.IntegerField(null=True, blank=True, verbose_name='AIT o Ictus Mimic', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='recanalizacdtc',
            field=models.IntegerField(null=True, blank=True, verbose_name='Recanalización doble transcraneal', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='aterovb',
            field=models.IntegerField(null=True, blank=True, verbose_name='Esteniosis VB significativa sintomática (ipsilateral al lado sintomático)', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='deterioro',
            field=models.IntegerField(null=True, blank=True, verbose_name='Deterioro', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='duplex_dtcipsilateral',
            field=models.IntegerField(null=True, blank=True, verbose_name='ESTENOSIS SIGNFICATIVAipsilateral (Vps >155 cm/s)', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='duplex_dtcotro',
            field=models.IntegerField(null=True, blank=True, verbose_name='ESTENOSIS significativa a cualquier otro nivel (vPS >155 CM/S)', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='ecocardiocardioembolico',
            field=models.IntegerField(null=True, blank=True, verbose_name='Ecocardio cardioembólico', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='ecocardiohecho',
            field=models.IntegerField(null=True, blank=True, verbose_name='Ecocardio realizado', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='ecodilatacionai',
            field=models.IntegerField(null=True, blank=True, verbose_name='Dilatación auricular izquierda', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='ecosta50ipsi',
            field=models.IntegerField(null=True, blank=True, verbose_name='ECOTSA>50% ipsilatearl', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='fluctuacion',
            field=models.IntegerField(null=True, blank=True, verbose_name='Fluctuación', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='holter',
            field=models.IntegerField(null=True, blank=True, verbose_name='Holter', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='holter_fa',
            field=models.IntegerField(null=True, blank=True, verbose_name='Rachas de FA o FAP  en Holter', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='mejoriaNIHSS4ev',
            field=models.IntegerField(null=True, blank=True, verbose_name='EV -Mejoria de 4 puntos o mas en la escala nihss', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='mejoriaNIHSS4ia',
            field=models.IntegerField(null=True, blank=True, verbose_name='IA - Mejoria de 4 puntos o mas en la escala nihss', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='monituifa',
            field=models.IntegerField(null=True, blank=True, verbose_name='DETECCION FA O FAP EN MONITORIZACION UI', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='reacanalizacdtc',
            field=models.IntegerField(null=True, blank=True, verbose_name='Recanalizacion durante rtpa', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='intervencion',
            name='transf_hemor',
            field=models.IntegerField(null=True, blank=True, verbose_name='Transformación hemorrágica', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='fop',
            field=models.CharField(null=True, blank=True, verbose_name='Presencia de foramen oval permeable', choices=[(0, 'No'), (1, 'Sí')], max_length=2),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='muertevascular',
            field=models.CharField(null=True, blank=True, verbose_name='Muerte de causa vascular', choices=[(0, 'No'), (1, 'Sí')], max_length=2),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='recurrencia',
            field=models.IntegerField(null=True, blank=True, verbose_name='Recurrencia', choices=[(0, 'No'), (1, 'Sí')]),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='recurrenciavasc',
            field=models.IntegerField(null=True, blank=True, verbose_name='Recurrencia vascular', choices=[(0, 'No'), (1, 'Sí')]),
        ),
    ]
