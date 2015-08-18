from django.shortcuts import render
from . import models
from django.views import generic
from datetime import datetime
from django.http import HttpResponse
from models import BlogEntry
# Create your views here.

class BlogIndex(generic.ListView):
    queryset = models.BlogEntry.objects.published()
    template_name = 'home.html'
    paginate_by = 2


def current_datetime(request, pk, slug=None):
    html = "<html><body>No blogs Found</body></html>"
    blog_post = BlogEntry.objects.get(pk=pk)
    if blog_post:
        if slug:
            if blog_post.slug == slug:
                html = "<html><body><h3>Awesome!</h3><br/>It is now %s.</body></html>" % datetime.now()
            else:
                html = "<html><body>Improper slug!</body></html>"
        else:
            html = "<html><body><h3>Awesome!</h3><br/>It is now %s.</body></html>" % datetime.now()
    return HttpResponse(html)
