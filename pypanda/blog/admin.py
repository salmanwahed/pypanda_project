from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

class BlogAdmin(MarkdownModelAdmin):
    list_display = ('title', 'created_on')


admin.site.register(models.BlogEntry, BlogAdmin)