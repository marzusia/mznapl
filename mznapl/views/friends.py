from .base import BaseView
from ..models.links import Friend


class IndexFriendsView(BaseView):
    template_name = 'mznapl/friends/index.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'friends': Friend.objects.all(),
            'title': 'friends',
        }
