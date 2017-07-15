from processing.models import TrashCan
from processing.serializers import TrashCanSerializer, UserSerializer
from processing.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


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


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'trashcans': reverse('trashcan-list', request=request, format=format)
    })
