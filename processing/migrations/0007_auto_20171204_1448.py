# Generated by Django 2.0 on 2017-12-04 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0006_trashcan_bn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcan',
            name='owner',
            field=models.ForeignKey(db_constraint=False, default=6, on_delete=django.db.models.deletion.CASCADE, related_name='trashcans', to=settings.AUTH_USER_MODEL),
        ),
    ]
