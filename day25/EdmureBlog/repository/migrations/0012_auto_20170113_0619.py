# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01while_for-13 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0011_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AlterField(
            model_name='blog',
            name='site',
            field=models.CharField(max_length=32, unique=True, verbose_name='个人博客前缀'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=64, verbose_name='个人博客标题'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
