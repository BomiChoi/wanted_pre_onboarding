from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('companies.Country', related_name='companies', on_delete=models.PROTECT)
    region = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)
