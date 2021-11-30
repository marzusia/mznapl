from django.shortcuts import get_object_or_404

from .base import BaseView
from ..models.page import Page


class ShowPageView(BaseView):
    template_name = 'mznapl/page/show.jinja'

    def get_context_data(self, **kwargs):
        page = get_object_or_404(Page, slug=kwargs['slug'])
        return {
            **super().get_context_data(**kwargs),
            'page': page,
            'title': page.title.lower(),
        }
