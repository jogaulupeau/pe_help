from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from pe_help.settings import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pe_help.views.home', name='home'),
    # url(r'^pe_help/', include('pe_help.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^cj/', include('cahier_journal.url'),
    url(r'^cj/(?P<object>\w+)/(?P<id>\d+)/$', 'cahier_journal.views.show'),
    url(r'^cj/journee/(?P<annee>\d+)/(?P<mois>\d+)/(?P<jour>\d+)/$', 'cahier_journal.views.journee'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT}),
)
