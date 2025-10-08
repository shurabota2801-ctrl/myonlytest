from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    