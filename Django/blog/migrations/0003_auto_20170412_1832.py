# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 13:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170412_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='reminderTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 32, 16, 339725)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 32, 16, 339725)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='modifiedTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 32, 16, 339725)),
        ),
    ]
