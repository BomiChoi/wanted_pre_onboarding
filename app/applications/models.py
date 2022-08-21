from django.db import models


# Create your models here.
class Application(models.Model):
    user = models.ForeignKey('users.User', verbose_name='사용자', related_name='applications', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', verbose_name='채용공고', related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='지원일시', auto_now_add=True)

    class Meta:
        verbose_name = '지원현황'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_order_product')
        ]
