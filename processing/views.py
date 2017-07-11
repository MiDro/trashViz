from processing.models import TrashCan
from processing.serializers import TrashCanSerializer, UserSerializer
from processing.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from django.contrib.auth.models import User

class TrashList(generics.ListCreateAPIView):
    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
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

