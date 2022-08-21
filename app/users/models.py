from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(verbose_name="이름", max_length=10)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
