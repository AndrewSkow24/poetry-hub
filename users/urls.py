from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import (
    ProfileDetailView,
    RegistrationUserView,
    ProfileListView,
    ProfileUpdateView,
)
from django.contrib.auth.models import User

urlpatterns = [
    path("registration/", RegistrationUserView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path(
        "profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"
    ),
    path("profiles/", ProfileListView.as_view(), name="profiles_list"),
]
