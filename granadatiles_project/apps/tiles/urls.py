from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^tiles$', views.TileList.as_view(), name='tiles'),
    url(r'^collections$', views.CollectionList.as_view(), name='collections'),
    url(r'^groups$', views.GroupList.as_view(), name='groups'),
] 


