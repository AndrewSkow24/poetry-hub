from django.urls import path
from .views import PoemCreateView, PoemListView


urlpatterns = [
    path("create/", PoemCreateView.as_view(), name="poem_create"),
    path("", PoemListView.as_view(), name="poem_list"),
]
