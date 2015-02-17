from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sdtools.views.menupage'),
    url(r'^notification/', include('notification.urls', namespace='notification')),
    url(r'^admin/', include(admin.site.urls)),
)
