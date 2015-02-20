from datetime import timedelta

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
# from django.core.mail import send_mail

from .models import Notification, Update
from .forms import NotificationForm, UpdateForm


#def start_notification(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = StartNotificationForm(request.POST)
#        print(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            return HttpResponseRedirect('/notification/notification_information/')
#
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = StartNotificationForm()
#
#    return render(request, 'notification/start_notification.html', {'form': form})

def notifications(request):
    return render_to_response(
        'notification/notifications.html', {'notifications': Notification.objects.all()})


def notification(request, notification_id):
    return render_to_response(
        'notification/notification.html',
        {'notification': Notification.objects.get(id=notification_id),
            'updates': Update.objects.filter(notification__id=notification_id)})


def edit_notification(request, notification_id):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/notification/detail/')
    else:
        form = NotificationForm()

    return render_to_response(
        'notification/edit_notification.html',
        {'form': form})


def new_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            n = Notification()
            n.client = form.cleaned_data['client']
            n.ntype = form.cleaned_data['ntype']
            n.headline = form.cleaned_data['headline']
            n.ticket = form.cleaned_data['ticket']
            n.raised = form.cleaned_data['raised']
            n.requester = form.cleaned_data['requester']
            n.save()

            return HttpResponseRedirect('/notification/all/')
    else:
        form = NotificationForm()

    return render(request, 'notification/new_notification.html', {'form': form})


def new_update(request, notification_id):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            u = Update()
            u.notification = Notification.objects.get(pk=notification_id)
            u.update_number = 1
            u.updated_at = form.cleaned_data['updated_at']
            u.next_update_at = form.cleaned_data['next_update_at']
            u.content = form.cleaned_data['content']
            u.save()

            return HttpResponseRedirect('/notification/' + notification_id + '/')

    else:
        in_an_hour = timezone.now() + timedelta(hours=1)
        form = UpdateForm(initial={
            'notification': notification_id,
            'next_update_at': in_an_hour, })

        # render used instead of render_to_response as that resulted in 403 error
        # CSRF token missing or incorrect. - The view function uses RequestContext for the template, instead of Context
        return render(request, 'notification/new_update.html', {'form': form, 'notification': notification_id, })


def add_update(request, notification_id):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            u = Update()
            u.notification = Notification.objects.get(pk=notification_id)
            u.update_number = form.cleaned_data['update_number']
            u.updated_at = form.cleaned_data['updated_at']
            u.next_update_at = form.cleaned_data['next_update_at']
            u.content = form.cleaned_data['content']
            u.save()

            return HttpResponseRedirect('/notification/' + notification_id + '/')

    else:
        next_update_at = timezone.now() + timedelta(hours=1)
        number_of_updates = len(Update.objects.filter(notification__id=notification_id))
        if number_of_updates > 0:
            next_update_is_due = Update.objects.filter(notification__id=notification_id).get(update_number=number_of_updates).next_update_at
            next_update_at = next_update_is_due + timedelta(hours=1)
        update_number = number_of_updates + 1
        form = UpdateForm(initial={
            'notification': notification_id,
            'update_number': update_number,
            'updated_at': next_update_is_due,
            'next_update_at': next_update_at, })

        # render used instead of render_to_response as that resulted in 403 error
        # CSRF token missing or incorrect. - The view function uses RequestContext for the template, instead of Context
        return render(request, 'notification/add_update.html', {'form': form, 'notification': notification_id, })



def preview_email(request):
    client = request.GET.get('client', '')
    return render(request, 'notification/preview_email.html', {'client': client})



# From django site second Work With Forms example
#def contact(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':

# From django site second Work With Forms example
#def contact(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = ContactForm(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            sender = form.cleaned_data['sender']
#            cc_myself = form.cleaned_data['cc_myself']
#
#            recipients = ['info@example.com']
#            if cc_myself:
#                recipients.append(sender)
#
#            send_mail(subject, message, sender, recipients)
#            return HttpResponseRedirect('/workingwithforms/thanks/')
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = ContactForm()
#
#    #return render(request, 'workingwithforms/contact_manual_fields.html', {'form': form})
#    return render(request, 'workingwithforms/contact.html', {'form': form})


