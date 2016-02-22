from django.conf.urls import patterns, url
from apps.galleries.views import galleries

urlpatterns = [
    url(r'^$', galleries, name='sr-gallery')
]
