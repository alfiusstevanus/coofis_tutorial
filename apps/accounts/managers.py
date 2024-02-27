from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, username, email, password, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError(_("Users must submit a username"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        user = self.model(
            username=username, email=email, is_staff=is_staff, is_superuser=is_superuser
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, is_staff=True, is_superuser=True):
        if not username:
            raise ValueError(_("Superusers must have a username"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        user = self.create_user(
            username, email, password, is_staff=is_staff, is_superuser=is_superuser
        )
        user.save(using=self._db)
        return user
