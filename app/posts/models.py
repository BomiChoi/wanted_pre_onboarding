from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Post(models.Model):
    company = models.ForeignKey('companies.Company', related_name='posts', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    reward = models.IntegerField(validators=[MinValueValidator(0)])
    content = models.TextField()
    skill = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
