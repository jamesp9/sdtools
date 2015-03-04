from django.conf.urls import patterns, url

from . import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^all/$', views.notifications, name='notifications'),
    url(r'^(?P<notification_id>\d+)/$', views.notification, name='notification'),
    url(r'^(?P<notification_id>\d+)/add/$', views.add_update, name='add_update'),
    url(r'^(?P<notification_id>\d+)/new/$', views.new_update, name='new_update'),
    url(r'^(?P<notification_id>\d+)/preview/$', views.preview_notification, name='preview_notification'),
    url(r'^edit/(?P<notification_id>\d+)/$', views.edit_notification, name='edit_notification'),
    url(r'^new/$', views.new_notification, name='new_notification'),
)
