# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-31 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=250, verbose_name='Add Comment'),
        ),
    ]
