from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import ProfileDetailView
from django.contrib.auth.models import User

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
]
