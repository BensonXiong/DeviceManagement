# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dmanage', '0007_auto_20151224_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=128)),
                ('action', models.CharField(max_length=128)),
                ('dateAt', models.DateTimeField(null=True, blank=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('LastModifiedAt', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(to='Dmanage.Device')),
            ],
        ),
    ]
