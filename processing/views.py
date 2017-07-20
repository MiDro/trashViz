from processing.models import TrashCan
from rest_framework.renderers import JSONRenderer
from processing.serializers import TrashCanSerializer, UserSerializer
from processing.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse
import datetime
from datetime import timedelta
import pytz

def get_instance(s):
    return s[s.index('/')+1:s.index("/", s.index("/")+1)]
class Sensor():

    def __init__(self, data, num):
        self.instance = get_instance(data['n'])
        self.value    = data['n']['v']
        self.num      = num
class TrashList(generics.ListCreateAPIView):
    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrashDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

def format_time_iso(time):
    return time.isoformat()
def get_sensor_info(data):
    # Sets of readings
    readings = data['payload']['e']

    sensorID = data['header']['sensorID']
    trashcan = TrashCan.objects.get(sensorID=sensorID)

    month = datetime.datetime.now(tzinfo=pytz.UTC).month
    day   = datetime.datetime.now(tzinfo=pytz.UTC).day
    year  = datetime.datetime.now(tzinfo=pytx.UTC).year

    # Times:   2:00PM previous day
    #         10:00PM previous day
    #          6:00PM previous day
    times = [
        datetime.datetime(year, month, day, 14, 0, 0, 0, pytx.UTC) - timedelta(days=1),
        datetime.datetime(year, month, day, 20, 0, 0, 0, pytx.UTC) - timedelta(days=1),
        datetime.datetime(year, month, day, 6, 0, 0, 0, pytx.UTC)
    ]
    for i in range(len(times)):
        current_time = times[i]

        sensor1 = Sensor(readings[i][0], 1)
        sensor2 = Sensor(readings[i][1], 2)
        sensor3 = Sensor(readings[i][2], 3)

        sensors = [sensor1, sensor2, sensor3]
        if any([x < 0 for x in [sensor1.value, sensor2.value, sensor2.value]]):
            pass




@api_view(['PUT'])
def api_put(request, format=None):
    if request.method == 'PUT':
        info = dict(eval(request.body.decode('utf-8')))

        sensorID = info['header']['sensorID']
        trashcan = TrashCan.objects.get(sensorID=sensorID)


        trashcan.header  = info['header']
        trashcan.payload = info['payload']
        trashcan.save()
    return Response(TrashCanSerializer(trashcan).data)

"""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'trashcans': reverse('trashcan-list', request=request, format=format)
    })
"""
class APIRoot(APIView):
    """
        API Root
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'trashcans': reverse('trashcan-list', request=request, format=format)
        })
