from datetime import datetime, timedelta

from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy
from django.utils.feedgenerator import Atom1Feed

from ..models.post import Post
from ..models.base.choices import PostTag


class RssPostsFeed(Feed):
    title = 'mzna.pl posts'
    link = reverse_lazy('post.index')
    description = 'My latest posts on mzna.pl'
    author_name = 'marzena'
    author_link = 'https://mzna.pl'
    categories = [t[0] for t in PostTag.CHOICES]

    def items(self):
        start_date = datetime.today() - timedelta(weeks=2)
        return Post.objects.filter(created_at__gte=start_date).order_by('-created_at')

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at

    def item_categories(self, item):
        return [item.tag]


class AtomPostsFeed(RssPostsFeed):
    feed_type = Atom1Feed
    subtitle = RssPostsFeed.description
