from rest_framework import serializers
from apps.calendars.models import Calendar
from apps.accounts.models import Profile
from django.contrib.auth.models import User
from apps.accounts.serializers.user_serializers import UserRetrieveSerializer

class CalendarSerializer(serializers.ModelSerializer):
    # 3 ini menyimpan id-nya
    creator_id = serializers.IntegerField(write_only=True)
    admins = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), write_only=True)
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), write_only=True)

    creator = serializers.SerializerMethodField()
    admins_details = UserRetrieveSerializer(source='admins', many=True, read_only=True)
    members_details = UserRetrieveSerializer(source='members', many=True, read_only=True)

    def get_creator(self, obj):
        if obj.creator:
            serializer = UserRetrieveSerializer(obj.creator)
            return serializer.data
        return None

    class Meta:
        model = Calendar
        fields = ['creator_id','admins', 'members','id','nama', 'creator', 'admins_details', 'members_details']