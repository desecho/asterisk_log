from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'asterisk_log.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'asterisk_log.views.logout_view'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
