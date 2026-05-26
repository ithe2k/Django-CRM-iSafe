from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "employee_code", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Información Profesional",
            {
                "fields": ("role", "employee_code", "supervisor"),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Información Profesional",
            {
                "fields": ("role", "employee_code", "supervisor"),
            },
        ),
    )
