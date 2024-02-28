from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from apps.calendars.serializers.calendar_serializers import CalendarSerializer
from apps.calendars.models import Calendar
from rest_framework.response import Response

class CalendarListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CalendarSerializer

    def create(self, request):
        user = request.user
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = self.get_queryset()
        serializer = CalendarSerializer(data, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = Calendar.objects.all()
        return queryset
    
class CalendarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CalendarSerializer

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
            "Calendar has been deleted",
            status=status.HTTP_204_NO_CONTENT,
        )
    
    def get_queryset(self):
        user = self.request.user.id
        queryset = Calendar.objects.all()
        return queryset