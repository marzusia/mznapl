from django.db import models

from .base.abstracts import UpdatableModel


class GuestbookEntry(UpdatableModel):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=128,
    )
    url = models.CharField(
        blank=True,
        null=True,
        max_length=128,
    )
    body = models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )

    class Meta:
        verbose_name = 'Guestbook entry'
        verbose_name_plural = 'Guestbook entries'

    def __str__(self):
        return '%s: %s' % (self.name, self.body)
