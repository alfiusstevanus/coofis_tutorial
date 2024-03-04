from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from apps.events.serializers.event_serializers import EventSerializer

from apps.events.models import Event
from rest_framework.response import Response

class EventListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-start_date')

    # def create(self, request):
    #     user = request.user
    #     serializer = self.get_serializer(data= request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     data = self.get_queryset()
    #     serializer = EventSerializer(data, many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Event.objects.all().order_by('-start_date')
    #     return queryset
    
class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self,request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            "Event has been deleted",
            status=status.HTTP_204_NO_CONTENT,
        )
    
    def get_queryset(self):
        user = self.request.user
        print(user)
        # queryset = Event.objects.filter(nama=user)
        queryset = Event.objects.all()
        return queryset