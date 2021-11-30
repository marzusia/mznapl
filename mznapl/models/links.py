from django.db import models


class Friend(models.Model):
    label = models.CharField(
        max_length=128,
        unique=True,
    )
    url = models.CharField(
        max_length=128,
        unique=True,
    )
    note = models.CharField(
        max_length=128,
    )

    def __str__(self):
        return self.label
