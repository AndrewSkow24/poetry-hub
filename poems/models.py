from django.db import models
from django.conf import settings


class Poem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    body = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return f"{self.title} ({self.author})"
