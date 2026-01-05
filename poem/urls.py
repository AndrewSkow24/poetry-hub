from django.urls import path
from .views import (
    PoemCreateView,
    PoemListView,
    PoemDetailView,
    PoemUpdateView,
    PoemDeleteView,
)


urlpatterns = [
    path("create/", PoemCreateView.as_view(), name="poem_create"),
    path("", PoemListView.as_view(), name="poem_list"),
    path("<int:pk>/", PoemDetailView.as_view(), name="poem_detail"),
    path("<int:pk>/update/", PoemUpdateView.as_view(), name="poem_update"),
    path("<int:pk>/delete/", PoemDeleteView.as_view(), name="poem_delete"),
]
