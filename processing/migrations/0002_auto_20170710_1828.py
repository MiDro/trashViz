# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trashcan',
            options={},
        ),
        migrations.RemoveField(
            model_name='trashcan',
            name='status',
        ),
        migrations.AddField(
            model_name='trashcan',
            name='full_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='trashcan',
            name='lastUpdated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last updated'),
        ),
        migrations.AddField(
            model_name='trashcan',
            name='sensor1',
            field=models.FloatField(default=50.0),
        ),
        migrations.AddField(
            model_name='trashcan',
            name='sensor2',
            field=models.FloatField(default=80.0),
        ),
        migrations.AddField(
            model_name='trashcan',
            name='sensor3',
            field=models.FloatField(default=69.0),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='fillLevel',
            field=models.FloatField(default=44.0),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='info',
            field=models.CharField(default='swag', max_length=500),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='installDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='installed'),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='lastEmptied',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last emptied'),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='latitude',
            field=models.FloatField(default=37.7249),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='location',
            field=models.CharField(default='101 Estudillo Ave', max_length=400),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='longitude',
            field=models.FloatField(default=-122.1561),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='maxFill',
            field=models.FloatField(default=100.0),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='name',
            field=models.CharField(default='MiDro', max_length=30),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='percent',
            field=models.FloatField(default=44.0),
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='trashID',
            field=models.IntegerField(default='1'),
        ),
    ]