# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01while_for-10 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0010_article_read_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
