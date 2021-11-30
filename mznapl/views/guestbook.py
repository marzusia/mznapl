from .base import BaseView
from ..models.guestbook import GuestbookEntry


class IndexGuestbookView(BaseView):
    template_name = 'mznapl/guestbook/index.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'entries': GuestbookEntry.objects.all().order_by('-created_at'),
            'title': 'guestbook',
        }
