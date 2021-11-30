from django.db import models

from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Page(UpdatableModel, AutoSlugMixin):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=128,
        unique=True,
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
    hidden = models.BooleanField(
        default=False,
    )

    auto_slug_populate_from = 'title'

    def __str__(self):
        return self.title
