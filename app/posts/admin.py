from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'company',
        'position',
        'reward',
        'skill',
        'content',
        'created_at'
    )
