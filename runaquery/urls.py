from django.conf.urls import patterns, url

from runaquery import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^enterdata/$', views.enterdata, name='enterdata'),
)
