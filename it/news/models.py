from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("Категория", unique=True, max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:news_home_by_category', args=[self.slug])

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    # category = models.PositiveSmallIntegerField(("Категория"), choices=categorys, blank=False, default=1)
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="products", on_delete=models.CASCADE,default=1)
    slug = AutoSlugField(populate_from='title')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.slug}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments (models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', blank = True, null = True, related_name='comments_articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    text = models.TextField(verbose_name='Текст комментария')


