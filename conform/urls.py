from django.conf.urls import patterns, url

from conform import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^$', views.get_name, name='get_name'),
    url(r'^thanks/$', views.thanks, name='thanks'),
)
