from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('feeder.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home'),
    url(r'^log/(?P<slug>[\w-]+)$', 'detail', name='detail'),
    url(r'^preview_rst$', 'preview_rst', name='preview_rst'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)