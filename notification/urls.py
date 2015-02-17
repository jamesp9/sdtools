from django.conf.urls import patterns, url

from notification import views

# "url" "name" argument allows reference from templates
urlpatterns = patterns('',
    url(r'^all/$', views.notifications, name='notifications'),
    url(r'^(?P<notification_id>\d+)/$', views.notification, name='notification'),
    url(r'^start_notification/$', views.start_notification, name='start_notification'),
    url(r'^notification_information/$',
        views.notification_information, name='notification_information'),
    url(r'^add_update/$', views.add_update, name='add_update'),
    url(r'^preview_email/$', views.preview_email, name='preview_email'),
)
