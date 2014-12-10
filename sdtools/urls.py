from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdtools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sdtools.views.menupage'),
    #url(r'^hcg/', include('hcg.urls', namespace='hcg')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^workingwithforms/', include('workingwithforms.urls', namespace='workingwithforms')),
    url(r'^runaquery/', include('runaquery.urls', namespace='runaquery')),
    url(r'^notification/', include('notification.urls', namespace='notification')),
    url(r'^admin/', include(admin.site.urls)),
)
