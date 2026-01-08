from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
from django.urls import reverse


class Poem(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy("автор"),
        null=True,
        blank=True,
        related_name="poems",
    )
    title = models.CharField(max_length=100, verbose_name=gettext_lazy("Название"))
    content = models.TextField(verbose_name=gettext_lazy("Содержание"))
    history = models.TextField(
        verbose_name=gettext_lazy("История создания"), null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=gettext_lazy("дата и время создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=gettext_lazy("дата и время обновления")
    )

    def __str__(self):
        return f"{self.title} {self.author}"

    def get_absolute_url(self):
        return reverse("poem_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
        ordering = ["-created_at"]
