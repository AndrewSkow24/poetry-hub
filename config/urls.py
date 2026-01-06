from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("poem.urls")),
    path("accounts/", include("profiles.urls")),
]
