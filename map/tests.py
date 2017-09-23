import datetime

from django.utils import timezone
from django.test import TestCase

from .models import TrashCan


class TrashCanModelTests(TestCase):

    def test_was_published_recently_with_future_trashCan(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_can = TrashCan(lastEmptied=time)
        self.assertIs(future_can.was_published_recently(), False)
