from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^search/', include('haystack.urls')),
    url(r'^post/(?P<pk>\d+)/(?P<slug>.*)/$', views.current_datetime, name='test'),
    url(r'^post/(?P<pk>\d+)/$', views.current_datetime, name='test'),
]
