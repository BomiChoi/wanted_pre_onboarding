from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'name',
                'email',
            )
        }),
    )
    list_display = (
        'id',
        'username',
        'name',
        'email',
        "is_active",
        "is_staff",
        "is_superuser",
    )
