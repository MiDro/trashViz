from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from processing.models import TrashCan
from processing.serializers import TrashCanSerializer

##  do not do this is in the real test. 
@api_view(['GET', 'POST'])
def trash_list(request, format=None):
    """
    List all code trashcans, or create a new trashcan.
    """
    if request.method == 'GET':
        trashcans = TrashCan.objects.all()
        serializer = TrashCanSerializer(trashcans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrashCanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##  do not do this is in the real test. 
@api_view(['GET', 'PUT', 'DELETE'])
def trash_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a trashcan.
    """
    try: 
        trashcan = TrashCan.objects.get(pk=pk)
    except TrashCan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrashCanSerializer(trashcan)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TrashCanSerializer(trashcan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trashcan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


