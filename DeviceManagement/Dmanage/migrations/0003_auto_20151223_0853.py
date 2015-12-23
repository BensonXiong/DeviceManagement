# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0002_auto_20151223_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='borrower',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='originOwner',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
