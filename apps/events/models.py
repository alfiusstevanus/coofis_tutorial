from django.db import models
from apps.calendars.models import Calendar
from apps.attachments.models import Attachment


class Event(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='calendar')
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='attachment', blank=True, null=True)

    nama = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    agenda = models.TextField()
    tempat = models.CharField(max_length=255)
    dresscode = models.CharField(max_length=50)

    def __str__(self):
        return self.nama