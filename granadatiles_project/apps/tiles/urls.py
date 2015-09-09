from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^tiles/$', views.TileList.as_view(), name='tiles'),
    url(r'^collections/$', views.CollectionList.as_view(), name='collections'),
    url(r'^collections/(?P<pk>\d+)/groups/$', views.CollectionDetail.as_view(), name='collection-detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='group-detail'),
] 


