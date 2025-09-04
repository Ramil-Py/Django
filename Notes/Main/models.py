from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс', max_length=100)
    text = models.TextField('Текст', max_length=1250)
    date = models.DateField('Дата')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'