from django.apps import AppConfig


class MznaplConfig(AppConfig):
    name = 'mznapl'
    verbose_name = 'mzna.pl'

    def ready(self):
        from . import signals
