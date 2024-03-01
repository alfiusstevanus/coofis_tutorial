from rest_framework import serializers
from apps.events.models import Event
from apps.calendars.models import Calendar
from apps.attachments.models import Attachment
from apps.calendars.serializers.calendar_serializers import CalendarSerializer
from apps.attachments.serializers.attachment_serializers import AttachmentSerializer

class EventSerializer(serializers.ModelSerializer):
    calendar_id = serializers.IntegerField(write_only=True)
    attachment_id = serializers.IntegerField(write_only=True)
    calendar = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()
    
    def get_calendar(self, obj):
        if obj.calendar:
            serializer = CalendarSerializer(obj.calendar)
            return serializer.data
        return None
    
    def get_attachment(self, obj):
        if obj.attachment:
            serializer = AttachmentSerializer(obj.attachment)
            return serializer.data
        return None

    class Meta:
        model = Event
        fields = ['calendar_id', 'attachment_id','id','nama','agenda','tempat','dresscode','start_date','end_date','calendar','attachment']

    def create(self, validated_data):
        event = Event.objects.create(**validated_data) 

        return event

    def update(self, instance, validated_data):
        instance.calendar = validated_data.get('calendar', instance.calendar)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        instance.nama = validated_data.get('nama', instance.nama)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.agenda = validated_data.get('agenda', instance.agenda)
        instance.tempat = validated_data.get('tempat', instance.tempat)
        instance.dresscode = validated_data.get('dresscode', instance.dresscode)
        instance.save()
        return instance
