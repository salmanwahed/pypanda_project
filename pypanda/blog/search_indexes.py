__author__ = 'salman'

import datetime
from haystack import indexes
from blog.models import BlogEntry


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        return BlogEntry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_on__lte=datetime.datetime.now())
