from django.db import models
from django.utils import timezone
from jsonfield import JSONField
import collections
import datetime
MIDRO = 6

# Default date to see if a new instance of trash can
DEFAULT_DATE = datetime.datetime(1997, 5, 15, 7, 44)
DEFAULT_DEC  = -50
.0;
DEFAULT_STR  = '101 Estudillo Avenue'
DEFAULT_NME  = 'MiDro'
DEFAULT_INT  = -1

# Default values
def date_default():
    return DEFAULT_DATE

def json_default():
    """
        Default jsonfield
    """
    return {'foo': 'bar'}

def dec_default():
    return DEFAULT_DEC


class PhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    name   = models.CharField(max_length=70)
    role   = models.IntegerField()


# Create your models here.
class TrashCan(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='trashcans',
        on_delete=models.CASCADE,
        default=MIDRO,
        db_constraint=False)

    # Last emptied is when the workers actually take out the trash in the
    # morning, while last updated is the time the node last transmitted.
    # This gives the app the ability to tell viewers that the view has a
    # potential to not be current.
    lastEmptied = models.DateTimeField('last emptied', default=date_default)
    lastUpdated = models.DateTimeField('last updated', default=date_default)

    installDate = models.DateTimeField('installed',    default=date_default)

    # These sensor readings are the calculated ones from the times sent from
    # the node.
    sensor1   = models.DecimalField(max_digits=10, decimal_places=5, default=dec_default)
    sensor2   = models.DecimalField(max_digits=10, decimal_places=5, default=dec_default)
    sensor3   = models.DecimalField(max_digits=10, decimal_places=5, default=dec_default)

    # Calculated height of center of trashcan.
    fillLevel = models.DecimalField(max_digits=6,  decimal_places=3, default=dec_default)

    # Maximamum height of trash
    maxFill   = models.DecimalField(max_digits=6,  decimal_places=3, default=dec_default)

    # fillLevel / maxFill
    percent   = models.DecimalField(max_digits=6,  decimal_places=3, default=dec_default)

    # Whether or not everything is working
    status    = models.BooleanField(default=True)

    # Whether the trashcan is full or not
    fillStatus= models.BooleanField(default=False)

    # Location Information. 5 decimal places is needed for meter accuracy. Take
    # 7 to be safe.
    latitude  = models.DecimalField(max_digits=11, decimal_places=7, default=dec_default)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, default=dec_default)
    location  = models.CharField(max_length=400, default=DEFAULT_STR)

    # Identifiers
    trashID   = models.IntegerField(default=DEFAULT_INT)
    name      = models.CharField(max_length=100, default=DEFAULT_NME)
    messageID = models.CharField(max_length=200, default=DEFAULT_NME)
    sensorID  = models.CharField(max_length=50,  default=DEFAULT_NME)
    macAddress= models.CharField(max_length=50,  default=DEFAULT_NME)

    # Original Payload information. Not acually needed, can be removed in
    # production
    header  = JSONField(null=True, blank=True, default=json_default)
    payload = JSONField(null=True, blank=True, default=json_default)

    # Version Stuff
    bt      = models.IntegerField(default=DEFAULT_INT)
    v       = models.IntegerField(default=DEFAULT_INT)
    bn      = models.CharField(max_length=100, default=DEFAULT_STR)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.lastEmptied <= now
