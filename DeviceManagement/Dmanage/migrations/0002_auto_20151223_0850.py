# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='borrowedAt',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='returnAt',
            field=models.DateTimeField(blank=True),
        ),
    ]
