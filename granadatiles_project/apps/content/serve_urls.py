from django.conf.urls import url
from apps.content.views import flatpage

urlpatterns = [
    url(r'^(?P<url>.*)$', flatpage, name='django.contrib.flatpages.views.flatpage'),
]
