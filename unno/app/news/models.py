from django.db import models

from .constants import SourceWebsites

# Create your models here.


class News(models.Model):
    """新聞"""

    uid = models.PositiveIntegerField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="post ID",
    )
    title = models.CharField(
        max_length=128,
        verbose_name="標題",
    )
    content = models.TextField(
        verbose_name="內文",
    )
    img = models.URLField(
        blank=True,
        null=True,
        verbose_name="圖片",
    )
    source = models.IntegerField(
        choices=SourceWebsites,
        verbose_name="來源網站",
    )
    source_url = models.URLField(
        unique=True,
        verbose_name="來源網址",
    )
    post_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="推文時間",
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="創建時間",
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="更新時間",
    )

    class Meta:
        verbose_name = "新聞"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
