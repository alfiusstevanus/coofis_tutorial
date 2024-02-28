from rest_framework import serializers
from apps.attachments.models import Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file']

    def create(self, validated_data):
        return Attachment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
