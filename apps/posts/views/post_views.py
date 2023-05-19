from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from apps.posts.serializers.post_serializers import PostSerializers

from apps.posts.models import Post
from rest_framework.response import Response

# Create your views here.

class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers

    def create(self, request):
        user = request.user
        serializer = self.get_serializer(data= request.data, context={'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # print(request.user)
        data = self.get_queryset()
        serializer = PostSerializers(data, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(creator = user).order_by('-created_at')
        return queryset
    
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers

    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def update(self,request,*args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance, request.data)
        serializers.is_valid(raise_exception=True)
        self.perform_update(serializers)
        return Response(serializers.data, status=status.HTTP_200_OK)

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            "Data has been deleted",
            status=status.HTTP_204_NO_CONTENT,
        )
    
    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(creator=user)
        return queryset