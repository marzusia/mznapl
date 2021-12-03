"""conlangdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views.feed import RssPostsFeed, AtomPostsFeed
from .views.friends import IndexFriendsView
from .views.guestbook import IndexGuestbookView
from .views.page import ShowPageView
from .views.post import IndexPostView, ShowPostView
from .views.static import IndexView


urlpatterns = [
    path('posts', IndexPostView.as_view(), name='post.index'),
    path('posts/<slug:slug>', ShowPostView.as_view(), name='post.show'),
    path('guestbook', IndexGuestbookView.as_view(), name='guestbook.index'),
    path('friends', IndexFriendsView.as_view(), name='friends.index'),
    path('feed/rss', RssPostsFeed(), name='feed.rss'),
    path('feed/atom', AtomPostsFeed(), name='feed.atom'),
    path('<slug:slug>', ShowPageView.as_view(), name='page.show'),
    path('', IndexView.as_view(), name='index'),
]
