from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=25)
    slug = models.CharField('栏目网址', max_length=25)
    intro = models.TextField('栏目简介', default='')
    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='栏目'
        verbose_name_plural='栏目'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容',default='', blank=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

