from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_calendars')
    admins = models.ManyToManyField(User, related_name='admin_calendars')
    members = models.ManyToManyField(User, related_name='calendars')

    def __str__(self):
        return f"Calendar created by {self.creator}"