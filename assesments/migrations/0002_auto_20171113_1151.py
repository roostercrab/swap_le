# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 19:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 19, 51, 27, 647168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 19, 51, 27, 647168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='total_exam_duration',
            field=models.TimeField(null=True),
        ),
    ]