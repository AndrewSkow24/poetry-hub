from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ["email", "username", "pseudonym", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("pseudonym",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("pseudonym",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
