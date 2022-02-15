from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=64)


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    categorys = [
        (1, 'Программирование'),
        (2, 'Современные технологии'),
        (3, 'Кибербезопасность'),
        (4, 'Игры и игровые консоли')
    ]
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='категория', choices=categorys)
    slug = AutoSlugField(populate_from='title')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.slug}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

