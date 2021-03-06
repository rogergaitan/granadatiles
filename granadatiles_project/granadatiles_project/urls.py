from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.content.views import index, about_us, videos, compare_products, cement_vs_ceramic, color_palletes, search, flatpage
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from granadatiles_project.sitemaps import StaticViewSitemap, CollectionSiteMap, GroupSiteMap
from django.contrib.flatpages.sitemaps import FlatPageSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'flat':  FlatPageSitemap,
    'collections': CollectionSiteMap,
    'groups': GroupSiteMap
    }

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'customadmin/', include('apps.customadmin.serve_urls' , namespace="customadmin")),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/', include('apps.tiles.urls', namespace='tiles')),
    url(r'^api/', include('apps.content.urls', namespace='content')),
    url(r'^api/', include('apps.galleries.urls', namespace='galleries')),
    url(r'^api/', include('apps.news.urls', namespace='news')),
    url(r'^api/', include('apps.customadmin.urls', namespace='dashboard')),
    url(r'^api/', include('apps.orders.urls', namespace='orders')),
    url(r'^api/token/', views.obtain_auth_token),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name= 'robots.txt', content_type= 'text/plain')),
    url(r'^humans\.txt$', TemplateView.as_view(template_name= 'humans.txt', content_type= 'text/plain')),
    url(r'^google8b1eebced5a00fe1\.html$', TemplateView.as_view(template_name= 'google8b1eebced5a00fe1.html')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += i18n_patterns(
    url(r'^$', index, name='home'),
    url(_(r'^search/$'), search, name='search'),
    url(_(r'^about-us/$'), about_us, name='about_us'),
    url(_(r'^product-comparison/$'), compare_products, name='compare_products'),
    url(_(r'^cement-vs-ceramic/$'), cement_vs_ceramic, name='cement_vs_ceramic'),
    url(_(r'^color-palletes/$'), color_palletes, name='color_palletes'),
    url(r'^videos/$', videos, name='videos'),
    url(r'^api/', include('apps.cart.urls', namespace='cart')),
    url(_(r'^portfolio/'),
        include('apps.portfolio.serve_urls', namespace='sr-portfolio')),
    url(_(r'^collections/'),
        include('apps.tiles.serve_urls', namespace='sr-collections')),
    url(_(r'^news/'),
        include('apps.news.serve_urls', namespace='sr-news')),
    url(_(r'^gallery/'),
        include('apps.galleries.serve_urls', namespace='sr-galleries')),
     url(_(r'^cart/'),
        include('apps.cart.serve_urls', namespace='sr-cart')),
     #url(r'^', include('django.contrib.flatpages.urls')),
     url(r'^', include('apps.content.serve_urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
