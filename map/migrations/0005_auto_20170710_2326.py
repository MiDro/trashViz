# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20170710_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcan',
            name='trashID',
            field=models.IntegerField(default=1),
        ),
    ]
