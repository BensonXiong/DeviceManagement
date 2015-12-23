# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0003_auto_20151223_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(max_length=128, choices=[(b'Android', b'And'), (b'Iphone', b'Ios')]),
        ),
    ]
