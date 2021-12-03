from django.db import models
from django.urls import reverse

from .base.abstracts import UpdatableModel
from .base.choices import PostTag
from .base.mixins import AutoSlugMixin


class Post(UpdatableModel, AutoSlugMixin):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=128,
    )
    slug = models.SlugField(
        null=False,
        blank=True,
        db_index=True,
        max_length=128,
        unique=True,
    )
    body = models.TextField(
        blank=False,
        null=False,
    )
    tag = models.CharField(
        max_length=32,
        choices=PostTag.CHOICES,
    )

    auto_slug_populate_from = 'title'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post.show', kwargs={'slug': self.slug})
