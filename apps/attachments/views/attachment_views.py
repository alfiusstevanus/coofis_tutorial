from rest_framework import generics
from apps.attachments.models import Attachment
from apps.attachments.serializers.attachment_serializers import AttachmentSerializer

class AttachmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class AttachmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    lookup_field = 'id'
