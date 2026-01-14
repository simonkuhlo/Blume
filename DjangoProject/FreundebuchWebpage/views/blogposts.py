from django.db.models import QuerySet
from django.shortcuts import render

from ..models import BlogPost

def get_browser(request):
    """Returns the blogpost browser as a HTTPResponse object."""
    pass

def reader(request):
    """Returns the blogpost reader as a HTTPResponse object."""
    pass

def news_feed(request):
    """Returns the blogpost news feed as a HTTPResponse object."""
    context = {"blog_posts" : get_posts()}
    return render(request, "blog_posts/parts/news_feed.html", context)

def get_posts(start:int = 0, end:int = 5) -> QuerySet[BlogPost, BlogPost]:
    blog_posts = BlogPost.objects.all()[start:end]
    return blog_posts