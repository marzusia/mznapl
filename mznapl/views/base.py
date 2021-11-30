from django.views.generic import TemplateView

from ..models.page import Page


class BaseView(TemplateView):
    template_name = 'mznapl/base/base.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'pages': Page.objects.filter(hidden=False).values('title', 'slug'),
            'title': 'home',
        }
