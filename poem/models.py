from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy


class Poem(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy("автор"),
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=100, verbose_name=gettext_lazy("Название"))
    context = models.TextField(verbose_name=gettext_lazy("Содержание"))
    history = models.TextField(verbose_name=gettext_lazy("История создания"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=gettext_lazy("дата и время создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=gettext_lazy("дата и время обновления")
    )

    def __str__(self):
        return f"{self.title} {self.author}"
