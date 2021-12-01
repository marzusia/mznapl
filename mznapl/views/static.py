from django.shortcuts import get_object_or_404

from .base import BaseView
from ..models.page import Page


class IndexView(BaseView):
    template_name = 'mznapl/static/index.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'page': get_object_or_404(Page, homepage=True),
        }
