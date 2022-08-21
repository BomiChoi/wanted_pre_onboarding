from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(verbose_name='회사명', max_length=100)
    country = models.ForeignKey('companies.Country', verbose_name='국가', related_name='companies',
                                on_delete=models.PROTECT)
    region = models.CharField(verbose_name='지역', max_length=100)

    class Meta:
        verbose_name = '회사'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name='국가명', max_length=100)

    class Meta:
        verbose_name = '국가'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
