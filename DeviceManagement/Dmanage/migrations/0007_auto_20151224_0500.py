# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0006_device_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='originOwner',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='device',
            name='borrower',
        ),
    ]
