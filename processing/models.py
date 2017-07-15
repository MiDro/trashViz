from django.db import models
from django.utils import timezone
import datetime
MIDRO = 6

# Create your models here.


class TrashCan(models.Model):
    lastEmptied = models.DateTimeField('last emptied', default=timezone.now)
    lastUpdated = models.DateTimeField('last updated', default=timezone.now)
    sensor1 = models.FloatField(default=50.0)
    sensor2 = models.FloatField(default=80.0)
    sensor3 = models.FloatField(default=69.0)
    fillLevel = models.FloatField(default=44.0)
    percent = models.FloatField(default=44.0)
    full_status = models.BooleanField(default=True)
    latitude = models.FloatField(default=37.7249)
    longitude = models.FloatField(default=-122.1561)
    location = models.CharField(max_length=400, default='101 Estudillo Ave')
    info = models.CharField(max_length=500, default='swag')
    maxFill = models.FloatField(default=100.0)
    installDate = models.DateTimeField('installed', default=timezone.now)
    trashID = models.IntegerField(default='1')
    name = models.CharField(max_length=30, default='MiDro')
    owner = models.ForeignKey(
        'auth.User',
        related_name='trashcans',
        on_delete=models.CASCADE,
        default=MIDRO)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.lastEmptied <= now
