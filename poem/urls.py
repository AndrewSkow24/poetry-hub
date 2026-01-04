from django.urls import path
from .views import PoemListView


urlpatterns = [path("", PoemListView.as_view(), name="poem_list")]
