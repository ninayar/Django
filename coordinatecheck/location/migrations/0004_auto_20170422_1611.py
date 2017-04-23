# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_loc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regions',
            name='id',
        ),
        migrations.AlterField(
            model_name='regions',
            name='score',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
