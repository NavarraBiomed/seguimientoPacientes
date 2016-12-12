# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictus', '0031_auto_20161212_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervencion',
            old_name='ecocardiocardioembolico',
            new_name='ecocardiocardieombolico',
        ),
        migrations.RenameField(
            model_name='intervencion',
            old_name='ecosta50ipsi',
            new_name='ecotsa50ipsi',
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='fop',
            field=models.IntegerField(verbose_name='Presencia de foramen oval permeable', choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='muertevascular',
            field=models.IntegerField(verbose_name='Muerte de causa vascular', choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True),
        ),
    ]
