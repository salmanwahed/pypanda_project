from django.db import models
from django_markdown.models import MarkdownField
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
from django.utils.text import slugify

class BlogQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    body = MarkdownField()
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    objects = BlogQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def _title_is_ascii(self):
        return all(ord(ch) < 128 for ch in self.title)

    def _create_slug(self):
        if self._title_is_ascii():
            slug_title = '-'.join(self.title.lower().split())
        else:
            slug_title = '-'.join(self.title.lower().split())
        return slug_title

    @property
    def slug(self):
        return self._create_slug()

    def get_absolute_url(self):
        iri = '/post/%i/%s/' % (self.id, urlquote(self.slug))
        return iri_to_uri(iri)

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created_on"]

# class Category(models.Model):
