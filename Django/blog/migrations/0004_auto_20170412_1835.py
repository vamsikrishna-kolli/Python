# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 13:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170412_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 35, 0, 496990)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='modifiedTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 35, 0, 496990)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='reminderTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 18, 35, 0, 496990)),
        ),
    ]
