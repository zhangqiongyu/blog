# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

def scramble_upload_img_name(instance, img_name):
    """
    Use the universally unique identifier (UUID) to unique the name of image
    """
    extension = img_name.split('.')[-1]
    return '{}.{}'.format(uuid.uuid4(), extension)

@python_2_unicode_compatible
class Category(models.Model):
    """"
    The category of articles
    """

    name = models.CharField('类目名称', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    owner = models.ForeignKey(
        'auth.User', verbose_name='作者', related_name='categories', on_delete=models.CASCADE
    )

    def __str__(self):
        return unicode(self.name)

@python_2_unicode_compatible
class Tag(models.Model):
    """"
    The tags of article.
    Atttibute:
        name: The name of the tag.
        ...
    """

    name = models.CharField('标签名称', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    owner = models.ForeignKey(
        'auth.User', verbose_name='作者', related_name='tags', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    """
    The detail of the article.
    Attribute:
        title: The title of the Article.
        body: The Content of the Article.
        created_time: The created time of the Article.
            The kwarg 'auto_now_add' means that the timestamp won't be overrided.
        last_modified_time: The latest time when the article was modified.
            The kwagt 'auto_now' means that the timestamp will be overrided after modifying
        ...
    """

    STATUS_CHOICES = (
        ('Editing', 'Editing'),
        ('Published', 'Published')
    )

    bg_img = models.ImageField('标题背景', upload_to=scramble_upload_img_name, blank=True, null=True)
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    abstract = models.CharField(
        '摘要', max_length=54, blank=True, null=True, help_text="此为可选项，若为空格则摘取正文前50个字符"
    )
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=10, choices=STATUS_CHOICES)
    topped = models.BooleanField('是否置顶', default=False)
    views = models.PositiveIntegerField('点击量', default=0)
    category = models.ForeignKey(
        Category, verbose_name='分类', related_name='articles', null=True, on_delete=models.SET_NULL
    )
    tags = models.ManyToManyField(
        'Tag', verbose_name='标签集合', related_name='articles', blank=True
    )
    owner = models.ForeignKey(
        'auth.User', verbose_name='作者', related_name='articles', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        """The Meta class"""

        ordering = ['-last_modified_time']
