from rest_framework import serializers
from apps.events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'calendar', 'attachment', 'nama', 'start_date', 'end_date', 'agenda', 'tempat', 'address_code']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.calendar = validated_data.get('calendar', instance.calendar)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        instance.nama = validated_data.get('nama', instance.nama)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.agenda = validated_data.get('agenda', instance.agenda)
        instance.tempat = validated_data.get('tempat', instance.tempat)
        instance.address_code = validated_data.get('address_code', instance.address_code)
        instance.save()
        return instance
