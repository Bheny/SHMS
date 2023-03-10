from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Shepherd
from .serializers import ShepherdSerializer

class ShepherdList(APIView):
    """
    List all shepherds or create a new shepherd.
    """
    def get(self, request):
        shepherds = Shepherd.objects.all()
        serializer = ShepherdSerializer(shepherds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShepherdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShepherdDetail(APIView):
    """
    Retrieve, update or delete a shepherd instance.
    """
    def get_object(self, pk):
        try:
            return Shepherd.objects.get(pk=pk)
        except Shepherd.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        shepherd = self.get_object(pk)
        serializer = ShepherdSerializer(shepherd)
        return Response(serializer.data)

    def put(self, request, pk):
        shepherd = self.get_object(pk)
        serializer = ShepherdSerializer(shepherd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shepherd = self.get_object(pk)
        shepherd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
