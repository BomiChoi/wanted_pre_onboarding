from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'country',
        'region',
    )


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


