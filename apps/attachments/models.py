from django.db import models

class Attachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return self.name