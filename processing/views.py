from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from processing.models import TrashCan
from processing.serializers import TrashCanSerializer

class TrashList(APIView):
    """
    List all code trashcans, or create a new trashcan.
    """
    def get(self, request, format=None):
        trashcans = TrashCan.objects.all()
        serializer = TrashCanSerializer(trashcans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TrashCanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class TrashDetail(APIView):
    """
    Retrieve, update, or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return TrashCan.objects.get(pk=pk)
        except TrashCan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trashcan = self.get_object(pk)
        serializer = TrashCanSerializer(trashcan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        trashcan = self.get_object(pk)
        serializer = TrashCanSerializer(trashcan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trashcan = self.get_object(pk)
        trashcan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ##  do not do this is in the real test. 
# @api_view(['GET', 'POST'])
# def trash_list(request, format=None):
#     """
#     List all code trashcans, or create a new trashcan.
#     """
#     if request.method == 'GET':
#         trashcans = TrashCan.objects.all()
#         serializer = TrashCanSerializer(trashcans, many=True)
#         return Response(serializer.data)
# 
#     elif request.method == 'POST':
#         serializer = TrashCanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# ##  do not do this is in the real test. 
# @api_view(['GET', 'PUT', 'DELETE'])
# def trash_detail(request, pk, format=None):
#     """
#     Retrieve, update, or delete a trashcan.
#     """
#     try: 
#         trashcan = TrashCan.objects.get(pk=pk)
#     except TrashCan.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# 
#     if request.method == 'GET':
#         serializer = TrashCanSerializer(trashcan)
#         return Response(serializer.data)
#     
#     elif request.method == 'PUT':
#         serializer = TrashCanSerializer(trashcan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     elif request.method == 'DELETE':
#         trashcan.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


