from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100),
    text = models.TextField('Основной текст статьи'),
    date = models.DateTimeField('Дата', default=timezone.now),
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

