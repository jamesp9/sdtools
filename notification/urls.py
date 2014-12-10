from django.conf.urls import patterns, url

from notification import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^start_notification/$', views.start_notification, name='start_notification'),
    url(r'^notification_information/$', views.notification_information, name='notification_information'),
)
