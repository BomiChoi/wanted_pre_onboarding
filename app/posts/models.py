from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Post(models.Model):
    company = models.ForeignKey('companies.Company', verbose_name='회사', related_name='posts', on_delete=models.CASCADE)
    position = models.CharField(verbose_name='채용포지션', max_length=100)
    reward = models.IntegerField(verbose_name='채용보상금', validators=[MinValueValidator(0)])
    content = models.TextField(verbose_name='채용내용')
    skill = models.CharField(verbose_name='사용기술', max_length=100)
    created_at = models.DateTimeField(verbose_name='등록일시', auto_now_add=True)

    class Meta:
        verbose_name = '채용공고'
        verbose_name_plural = verbose_name
