# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0005_auto_20151223_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='slug',
            field=models.SlugField(default=1, unique=True, max_length=128),
            preserve_default=False,
        ),
    ]
