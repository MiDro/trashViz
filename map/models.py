from django.db import models

# Create your models here.
class TrashCan(models.Model):
    lastEmptied = models.DateTimeField('last emptied')
    installDate = models.DateTimeField('installed')
    fillLevel = models.FloatField()
    maxFill = models.FloatField()
    percent = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=400)
    trashID = models.IntegerField()
    status = models.BooleanField()
    info = models.CharField(max_length=500)
    name = models.CharField(max_length=30)
