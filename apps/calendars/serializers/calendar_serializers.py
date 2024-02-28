from rest_framework import serializers
from apps.calendars.models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'nama', 'creator', 'admins', 'members']

    def create(self, validated_data):
        admins_data = validated_data.pop('admins', [])  #ambil admin jika ada
        members_data = validated_data.pop('members', [])

        #buat kalender
        calendar = Calendar.objects.create(**validated_data)

        #tambah admin
        for admin_data in admins_data:
            calendar.admins.add(admin_data)
        for member_data in members_data:
            calendar.members.add(member_data)

        return calendar

    # def update(self, instance, validated_data):
    #     instance.creator = validated_data.get('creator', instance.creator)
        
    #     #hapus semua admin
    #     instance.admins.clear()
    #     #tambah admin baru
    #     admins_data = validated_data.get('admins', [])
    #     for admin_data in admins_data:
    #         instance.admins.add(admin_data)
        
    #     #hapus semua member
    #     instance.members.clear()
    #     #tambah member baru
    #     members_data = validated_data.get('members', [])
    #     for member_data in members_data:
    #         instance.members.add(member_data)

    #     instance.save()
    #     return instance
