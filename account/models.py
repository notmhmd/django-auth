from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.db import models

USER = 1
STAFF = 2
ADMIN = 3

ROLE_CHOICES = (
    (USER, 'user'),
    (STAFF, 'staff'),
    (ADMIN, 'admin'),
)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), blank=True, unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def type(self):
        if self.is_superuser:
            return "admin"

        if self.is_staff:
            return "staff"

        return "user"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(verbose_name="Date Of Birth", blank=True, null=True)

    def __str__(self):
        return " ".join([self.user.first_name, self.user.last_name])
