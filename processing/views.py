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
from decimal import Decimal
from datetime import timedelta
import pytz


from .message import send_message

SPEED_OF_SOUND = 343 * 1000 # cm/s
DEBUG_MODE = True
class Sensor():

    def __init__(self, data, num):
        self.instance = data['n'][data['n'].index('/')+1:
                        data['n'].index("/", data['n'].index("/")+1)]
        if 'v' in data:
            self.value    = int(data['v'])
        elif 'bv' in data:
            self.value    = -1
        else:
            self.value    = -1
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

def get_distance(time):
    # Velocity = Distance / Time
    # So, Distance = Velocity * Time
    time_secs = time / 1e6
    return SPEED_OF_SOUND * time_secs


def parse_can(data):
    if not DEBUG_MODE:
        # Sets of readings
        readings = data['payload']['e']

        sensorID = data['header']['sensorID']
        trashcan = TrashCan.objects.get(sensorID=sensorID)
        trashcan.bt = data['payload'].get('bt')
        trashcan.v  = data['payload'].get('ver')
        trashcan.bn = data['payload'].get('bn')

        month = datetime.datetime.now(pytz.UTC).month
        day   = datetime.datetime.now(pytz.UTC).day
        year  = datetime.datetime.now(pytz.UTC).year

        # Times:   2:00PM previous day
        #         10:00PM previous day
        #          6:00PM previous day
        times = [
            datetime.datetime(year, month, day, 14, 0, 0, 0, pytz.UTC) - timedelta(days=1),
            datetime.datetime(year, month, day, 20, 0, 0, 0, pytz.UTC) - timedelta(days=1),
            datetime.datetime(year, month, day, 6, 0, 0, 0,  pytz.UTC)
        ]
        now = times[2] # Time of last transmit
        for i in range(len(times)):
            current_time = times[i]

            sensor0 = Sensor(readings[i][0], 0)
            sensor1 = Sensor(readings[i][1], 1)
            sensor2 = Sensor(readings[i][2], 2)

            sensors = [sensor0, sensor1, sensor2]

            # Sensor error checking

            dists  = [ get_distance(sensor0.value), get_distance(sensor1.value), get_distance(sensor2.value)]
            trashcan.sensor1 = dists[0]
            trashcan.sensor2 = dists[1]
            trashcan.sensor3 = dists[2]

            # If any of the sensors have a negative value
            if any([x < 0 for x in dists]):
                trashcan.status = False # This trashcan is not fully functional

                # TODO: WHat to do if sensors have errors

            else:
                trashcan.status = True

                trashcan.fillLevel = Decimal(sum(dists)/len(dists))
                trashcan.percent   = trashcan.fillLevel / trashcan.maxFill * 100

                trashcan.fillStatus= trashcan.percent > 70


            # PI Web API stuff
        trashcan.lastUpdated = now

        trashcan.save()
    else:
        # Sets of readings
        readings = data['payload']['e']

        sensorID = data['header']['sensorID']
        trashcan = TrashCan.objects.get(sensorID=sensorID)
        trashcan.bt = data['payload'].get('bt')
        trashcan.v  = data['payload'].get('ver')
        trashcan.bn = data['payload'].get('bn')

        sensor0 = Sensor(readings[0], 0)
        sensor1 = Sensor(readings[1], 1)
        sensor2 = Sensor(readings[2], 2)

        sensors = [sensor0, sensor1, sensor2]

        # Sensor error checking

        dists  = [ get_distance(sensor0.value), get_distance(sensor1.value), get_distance(sensor2.value)]
        trashcan.sensor1 = dists[0]
        trashcan.sensor2 = dists[1]
        trashcan.sensor3 = dists[2]

        # If any of the sensors have a negative value
        if any([x < 0 for x in dists]):
            trashcan.status = False # This trashcan is not fully functional
            send_message("The trash can is out of order.")
        else:
            trashcan.status = True

            trashcan.fillLevel = Decimal(sum(dists)/len(dists))
            trashcan.percent   = trashcan.fillLevel / trashcan.maxFill * 100

            send_message("The trash can is {}% full".format(int(trashcan.percent)))
            trashcan.fillStatus= trashcan.percent > 70

        trashcan.lastUpdated = datetime.datetime.now()
        
        trashcan.save()
@api_view(['PUT'])
def api_put(request, format=None):
    if request.method == 'PUT':
        try:
            info = dict(eval(request.body.decode('utf-8')))
        except:
            return Response({
              "error_code": 500,
              "message": "No body in request"
            })
        sensorID = info['header']['sensorID']
        try:
            trashcan = TrashCan.objects.get(sensorID=sensorID)
        except:
            return Response({
              "error_code": 401,
              "message": "Authentication failure"
            })


        trashcan.header  = info['header']
        trashcan.payload = info['payload']
        trashcan.save()
        try:
            parse_can(info)
        except:
            return Response({
              "error_code":500,
              "message": "Data saving error"
            })
        trashcan.save()
    return Response(TrashCanSerializer(trashcan).data, status=201)

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
