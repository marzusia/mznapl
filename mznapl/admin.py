from django.contrib import admin

from . import models


for model in [getattr(models, m) for m in models.__all__]:
    admin.site.register(model)
