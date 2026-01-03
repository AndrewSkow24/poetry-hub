from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.core.validators import RegexValidator
from django.conf import settings


class User(AbstractUser):
    """
    Модифицированная модель пользователя (расширение стандартной модели)
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False,
        verbose_name=gettext_lazy("ID"),
    )
    email = models.EmailField(
        gettext_lazy("email адрес"),
        unique=True,
        db_index=True,
        error_messages={
            "unique": gettext_lazy("Пользователь с таким email уже существует")
        },
    )
    username = models.CharField(
        gettext_lazy("имя пользователя"),
        max_length=150,
        unique=True,
        help_text=gettext_lazy(
            "Обязательное поле 150 символов. Только буквы, цифры и @/./_/+/-_."
        ),
        error_messages={
            "unique": gettext_lazy("Пользователь с таким именем уже существует.")
        },
    )
    bio = models.TextField(
        gettext_lazy("Биография"),
        max_length=500,
        blank=True,
        help_text=gettext_lazy("Расскажите о себе (максимум 500 символов)."),
    )
    avatar = models.ImageField(
        gettext_lazy("аватар"),
        upload_to="avatars/%Y/&m/&d/",
        blank=True,
        null=True,
        help_text=gettext_lazy("Загрузите изображение для вашего аватара"),
    )
    website = models.URLField(
        gettext_lazy("Веб-сайт"),
        max_length=200,
        blank=True,
        help_text=gettext_lazy("Ссылка на ваш веб-сайт или блог."),
    )
