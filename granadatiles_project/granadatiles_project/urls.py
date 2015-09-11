from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.content import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/', include('apps.tiles.urls', namespace='tiles')),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.index, name='home'),
    url(_(r'^collections/'), include('apps.tiles.serve_urls' , namespace='sr-collections'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
