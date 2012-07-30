from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tokenmanager.views.index', name='index'),
    url(r'^channel$', 'tokenmanager.views.channel', name='channel'),
    url(r'^token$', 'tokenmanager.views.token', name='token'),

    #url(r'^fbtoken/', include('fbtoken.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# DEBUG/local dev only:
urlpatterns += staticfiles_urlpatterns()
