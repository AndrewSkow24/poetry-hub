from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PoemConfig(AppConfig):
    name = "poem"
    verbose_name = gettext_lazy("Стихи")
