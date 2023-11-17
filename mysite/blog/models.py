from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    # это короткая метка, содержащая только буквы, цифры,
    # знаки подчеркивания или дефисы.
    # Было Django Reinhardt: A legend of Jazz
    # Слаг django-reinhardt-legend-jazz

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

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
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title




# python manage.py shell
#
# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from  blog.models import Post
#
#
#
# .objects.get
# user = User.objects.get(username='devmanyur')
# DoesNotExist - нет объекта
# MultipleObjectsReturned - много объектов
#
# >>>> save() <<<
# post3 = Post(title='Who Another post3',slug='Who-another-post3', body='Who  Post body3.', author=user)
# post3.save()
#
#
# .objects.all()
# Post.objects.all()
#
#
# .objects.filter()
# Post.objects.filter(publish__year=2023, author__username='devmanyur')
#
#
# exclude() исключать
# Post.objects.filter(publish__year=2022).exclude(title__startswith='Why')
#
#
# order_by() сортировка
# Post.objects.order_by('title')
# Post.objects.order_by('-title')
#
#
#delete() удалить
# post = Post.objects.get(id=1)
# post.delete()

