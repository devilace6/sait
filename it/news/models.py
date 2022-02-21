from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

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

