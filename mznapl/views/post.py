from django.shortcuts import get_object_or_404

from .base import BaseView
from ..models.post import Post


class IndexPostView(BaseView):
    template_name = 'mznapl/post/index.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'posts': Post.objects.all().order_by('-created_at'),
            'title': 'posts',
        }


class ShowPostView(BaseView):
    template_name = 'mznapl/post/show.jinja'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        return {
            **super().get_context_data(**kwargs),
            'post': post,
            'title': post.title.lower(),
        }
