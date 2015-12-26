# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0008_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='imei',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='device',
            name='sn',
            field=models.CharField(max_length=128),
        ),
    ]
