# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0004_auto_20170718_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashcan',
            name='bt',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='trashcan',
            name='v',
            field=models.IntegerField(default=-1),
        ),
    ]
