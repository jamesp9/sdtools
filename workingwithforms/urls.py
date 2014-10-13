from django.conf.urls import patterns, url

from workingwithforms import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^get_name/$', views.get_name, name='get_name'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
)
