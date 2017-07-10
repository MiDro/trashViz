# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrashCan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastEmptied', models.DateTimeField(verbose_name='last emptied')),
                ('installDate', models.DateTimeField(verbose_name='installed')),
                ('fillLevel', models.FloatField()),
                ('maxFill', models.FloatField()),
                ('percent', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('location', models.CharField(max_length=400)),
                ('trashID', models.IntegerField()),
                ('status', models.BooleanField()),
                ('info', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('percent',),
            },
        ),
    ]
