from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class TrashCan(models.Model):
    lastEmptied = models.DateTimeField('last emptied')
    installDate = models.DateTimeField('installed')
    fillLevel = models.FloatField()
    maxFill = models.FloatField()
    percent = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=400)
    trashID = models.IntegerField()
    status = models.BooleanField()
    info = models.CharField(max_length=500)
    name = models.CharField(max_length=30)


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.lastEmptied <= now
