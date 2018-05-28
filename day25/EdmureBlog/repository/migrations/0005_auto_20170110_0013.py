# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01while_for-10 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20170109_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='repository.Article2Tag', to='repository.Tag'),
        ),
        migrations.AlterField(
            model_name='article2tag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Tag'),
        ),
        migrations.AlterField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article'),
        ),
    ]
