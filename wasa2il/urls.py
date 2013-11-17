
from django.conf.urls.defaults import patterns, include, url
from django.shortcuts import redirect
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

RSK_URL = 'https://www.island.is/audkenning?id=piratar.is'


urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Enabling i18n language changes per
        # https://docs.djangoproject.com/en/1.4/topics/i18n/translation/#the-set-language-redirect-view
        (r'^i18n/', include('django.conf.urls.i18n')),

    # Core app
    (r'^', include('wasa2il.core.urls')),
    # Forums app
    (r'^', include('wasa2il.forum.urls')),

    (r'^accounts/profile/(?:(?P<username>.+)/)?$', 'core.views.profile'),
    (r'^accounts/settings/', 'core.views.view_settings'),
    (r'^accounts/register/', lambda r: redirect(RSK_URL)),
    (r'^accounts/', include('registration.urls')),

    (r'^help/$', direct_to_template, {"template": "help/index.html"}),
    (r'^help/(?P<page>.*)/$', "core.views.help"),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
