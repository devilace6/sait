from django.db import models
from autoslug import AutoSlugField


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.slug}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

