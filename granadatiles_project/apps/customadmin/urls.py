# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^search$', 'apps.customadmin.views.search', name="search"),
)