# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('imei', models.CharField(unique=True, max_length=128)),
                ('sn', models.CharField(unique=True, max_length=128)),
                ('originOwner', models.CharField(default=b'', max_length=128)),
                ('borrower', models.CharField(max_length=128)),
                ('borrowedAt', models.DateTimeField()),
                ('returnAt', models.DateTimeField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('LastModifiedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
