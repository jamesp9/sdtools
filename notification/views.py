from datetime import timedelta

from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
# from django.core.mail import send_mail

from .models import Notification, Update
from .forms import NotificationForm, UpdateForm


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
    number_of_updates = len(Update.objects.filter(notification__id=notification_id))
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            u = Update()
            u.notification = Notification.objects.get(pk=notification_id)
            u.update_number = number_of_updates + 1
            u.updated_at = form.cleaned_data['updated_at']
            u.next_update_at = form.cleaned_data['next_update_at']
            u.content = form.cleaned_data['content']
            u.save()

            return HttpResponseRedirect('/notification/' + notification_id + '/')

    else:
        if number_of_updates > 0:
            # Prefill "updated at" with the "next update" time from previous Update
            updated_at = Update.objects.filter(notification__id=notification_id).get(
                update_number=number_of_updates).next_update_at
        else:
            updated_at = timezone.now()

        next_update_at = updated_at + timedelta(hours=1)

        update_number = number_of_updates + 1

        form = UpdateForm(initial={
            'notification': notification_id,
            'update_number': update_number,
            'updated_at': updated_at,
            'next_update_at': next_update_at, })

        # render used instead of render_to_response as that resulted in 403 error
        # CSRF token missing or incorrect. - The view function uses RequestContext for the template, instead of Context
        return render(request, 'notification/add_update.html', {'form': form, 'notification': notification_id, })


def preview_email(request):
    client = request.GET.get('client', '')
    return render(request, 'notification/preview_email.html', {'client': client})


def preview_notification(request, notification_id):
    email_template = get_template('notification/notification_email.html')
    # email_subject = "Client - Notification Type - Ticket - Headline - Update No."
    email_html = email_template.render(Context({
        'notification': Notification.objects.get(id=notification_id),
        'updates': Update.objects.filter(notification__id=notification_id).order_by('-update_number')
    }))
    return render(
        request,
        'notification/notification_preview.html',
        {'notification': Notification.objects.get(id=notification_id), 'email_html': email_html, })
