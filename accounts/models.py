from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pseudonym = models.CharField(
        null=True, blank=True, max_length=100, verbose_name="псевдоним"
    )
