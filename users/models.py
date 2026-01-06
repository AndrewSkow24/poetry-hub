from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        related_name="profile",
    )

    avatar = models.ImageField(
        upload_to="avatars", verbose_name="аватар", blank=True, null=True
    )
    bio = models.TextField(verbose_name="о себе", blank=True, null=True)
    pseudonym = models.CharField(
        max_length=150, verbose_name="псевдоним", blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата и время обновления"
    )

    class Meta:
        verbose_name = "профиль"
        verbose_name = "профили"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Профиль "
