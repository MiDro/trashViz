# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 22:25
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields
import processing.models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0007_auto_20170715_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcan',
            name='payload',
            field=jsonfield.fields.JSONField(blank=True, default=processing.models.my_default, null=True),
        ),
    ]
