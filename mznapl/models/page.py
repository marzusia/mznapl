from django.db import models
from django.utils.translation import gettext_lazy as _

from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Page(UpdatableModel, AutoSlugMixin):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=128,
        unique=True,
        help_text=_('The title of the page'),
    )
    slug = models.SlugField(
        null=False,
        blank=True,
        db_index=True,
        max_length=128,
        unique=True,
        help_text=_('The URL identifier for the page. Leave blank to auto-generate.'),
    )
    body = models.TextField(
        blank=False,
        null=False,
        help_text=_('What should this page say? You should use HTML tags.'),
    )
    show_in_nav = models.BooleanField(
        default=False,
        help_text=_('Should this page show up as a link in the main navigation bar?'),
        db_index=True,
    )
    homepage = models.BooleanField(
        default=False,
        help_text=_('Should this page\'s content be displayed as the homepage?'),
    )

    auto_slug_populate_from = 'title'

    def __str__(self):
        return self.title
