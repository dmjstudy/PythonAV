# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01while_for-10 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0009_auto_20170110_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
    ]
