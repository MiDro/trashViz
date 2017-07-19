from processing.models import TrashCan
from processing.serializers import TrashCanSerializer, UserSerializer
from processing.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from django.views.generic import View
import datetime
from datetime import timedelta
import pytz

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

def get_sensor_info(data):
    # Sets of readings
    readings = data['payload']['e']

    month = datetime.datetime.now(tzinfo=pytz.UTC).month
    day   = datetime.datetime.now(tzinfo=pytz.UTC).day
    year  = datetime.datetime.now(tzinfo=pytx.UTC).year
    times = [
        datetime.datetime(year, month, )
    ]
    for i in range(len(readings)):
        pass

@api_view(['PUT'])
def api_put(request, format=None):
    if request.method == 'PUT':
        info = dict(eval(request.body.decode('utf-8')))

        sensorID = info['head']['sensorID']
        trashcan = TrashCan.objects.get(sensorID=sensorID)


    return Response({
        'users': reverse('user-list', request=request, format=format),
        'trashcans': reverse('trashcan-list', request=request, format=format)
    })

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

"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'trashcans': reverse('trashcan-list', request=request, format=format)
    })

"""
