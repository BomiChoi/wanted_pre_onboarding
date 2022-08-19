from django.db import models


# Create your models here.
class Application(models.Model):
    user = models.ForeignKey('users.User', related_name='applications', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
