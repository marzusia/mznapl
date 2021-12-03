from datetime import datetime, timedelta

from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy

from ..models.post import Post


class LatestPostsFeed(Feed):
    title = 'mzna.pl posts'
    link = reverse_lazy('post.index')
    description = 'My latest posts on mzna.pl'

    def items(self):
        start_date = datetime.today() - timedelta(weeks=2)
        return Post.objects.filter(created_at__gte=start_date).order_by('-created_at')

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at

    def item_categories(self, item):
        return [item.tag]
