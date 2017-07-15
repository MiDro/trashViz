# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 22:14
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields
import processing.models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0005_trashcan_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashcan',
            name='paylod',
            field=jsonfield.fields.JSONField(default=processing.models.my_default),
        ),
    ]
