import uuid
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Profile(TimeStampedUUIDModel):
    class JenisKelamin(models.TextChoices):
        MALE = "Laki-Laki", _("Laki-Laki")
        FEMALE = "Perempuan", _("Perempuan")
    jenis_kelamin = models.CharField(max_length=255,choices=JenisKelamin.choices,default=None, blank=True, null=True)
    username = models.CharField(verbose_name=_("username"), help_text=_("username"), max_length=255, unique=True)
    email = models.EmailField(verbose_name=_("email address"), db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # USERNAME_FIELD = "nim"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "accounts_user"
