# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0004_auto_20151223_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='borrowedAt',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='returnAt',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
