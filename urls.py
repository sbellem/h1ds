"""Base URLs for H1DS project.

This module provides a small number of urls, and forwards app-specific URLS to the relevant apps.

URLS provided by this module:

* '^robots\.txt$' -- tell web-crawlers (Google et al.) which which areas to leave alone.
* '^admin/doc/'   -- docs for admin interface
* '^admin/'       -- admin interface
* '^openid/'      -- OpenID authentication

URLS passed to other H1DS modules.

* '' -- all queries are first checked against h1ds_core for a match.




"""
import sys

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

from h1ds import AVAILABLE_H1DS_MODULES
from h1ds.views import TextTemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^robots\.txt$', TextTemplateView.as_view(template_name='robots.txt')),
                       (r'', include('h1ds_core.urls')),
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^openid/', include('django_openid_auth.urls')),
                       )

for mod_name in AVAILABLE_H1DS_MODULES:
    if mod_name in settings.INSTALLED_APPS:
        mod = __import__(mod_name)
        urlpatterns += patterns('',
        (r'^{}/'.format(mod.MODULE_ROOT_URL), 
         include('{}.urls'.format(mod_name))),
            )
                                

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                }
            ),
    )
