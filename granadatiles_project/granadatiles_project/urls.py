from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.content.views import index, about_us, videos, compare_products, cement_vs_ceramic, color_palletes
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'customadmin/', include('apps.customadmin.urls' , namespace="customadmin")),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/', include('apps.tiles.urls', namespace='tiles')),
    url(r'^api/', include('apps.content.urls', namespace='content')),
    url(r'^api/', include('apps.galleries.urls', namespace='galleries')),
    url(r'^api/', include('apps.news.urls', namespace='news')),
    url(r'^api/', include('apps.quickbooks.urls', namespace='quickbooks')),
    url(r'^api/', include('apps.customadmin.urls', namespace='dashboard')),
    url(r'^api/token/', views.obtain_auth_token),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += i18n_patterns(
    url(r'^$', index, name='home'),
    url(_(r'^about-us/$'), about_us, name='about_us'),
    url(_(r'^compare-our-products/$'), compare_products, name='compare_products'),
    url(_(r'^cement-vs-ceramic/$'), cement_vs_ceramic, name='cement_vs_ceramic'),
    url(_(r'^color-palletes/$'), color_palletes, name='color_palletes'),
    url(_(r'^collections/'),
        include('apps.tiles.serve_urls', namespace='sr-collections')),
    url(_(r'^news/'),
        include('apps.news.serve_urls', namespace='sr-news')),
    url(_(r'^gallery/'),
        include('apps.galleries.serve_urls', namespace='sr-galleries'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
