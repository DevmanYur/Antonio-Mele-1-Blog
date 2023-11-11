from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    # это короткая метка, содержащая только буквы, цифры,
    # знаки подчеркивания или дефисы.
    # Было Django Reinhardt: A legend of Jazz
    # Слаг django-reinhardt-legend-jazz
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # По умолчанию значения поля задаются
    # методом Django timezone.now.

    created = models.DateTimeField(auto_now_add=True)
    # При применении параметра
    # auto_now_add дата будет сохраняться автоматически во время создания
    # объекта

    updated = models.DateTimeField(auto_now=True)
    # При применении
    # параметра auto_now дата будет обновляться автоматически во время
    # сохранения объекта.

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
