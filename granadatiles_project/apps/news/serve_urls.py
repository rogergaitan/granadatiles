from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.news.views import news

urlpatterns = [
    url(_(r'^articles/$'), news, name='sr-news')
]
