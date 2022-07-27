from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
    )
    list_display = ("email", "username", "first_name", "last_name", "is_staff",)
    search_fields = ("email", "first_name", "last_name",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)