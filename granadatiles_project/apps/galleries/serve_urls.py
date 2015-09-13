from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.galleries.views import galleries

urlpatterns = [
    url(r'^$', galleries, name='sr-gallery')
]
