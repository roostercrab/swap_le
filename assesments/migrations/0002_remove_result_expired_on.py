# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='expired_on',
        ),
    ]
