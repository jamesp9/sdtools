from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail

from .models import Notification, Update
from .forms import NotificationForm


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


#def notification_information(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = NotificationInformationForm(request.POST)
#        print(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            return HttpResponseRedirect('/notification/notification_update/')
#
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = NotificationInformationForm()
#
#    return render(request, 'notification/notification_information.html',
#            {'form': form, 'request': request.META, 'post_data': request.POST})


def notification_information(request):
    client = request.GET.get('client_name', '')
    noti_type = request.GET.get('noti_type', '')

    form = NotificationInformationForm()

    return render(
        request,
        'notification/notification_information.html',
        {'form': form, 'client': client, 'noti_type': noti_type})


def add_update(request):
    client = request.GET.get('client', '')
    noti_type = request.GET.get('noti_type', '')
    ticket_no = request.GET.get('ticket_no', '')
    headline = request.GET.get('headline', '')
    requestor_name = request.GET.get('requestor_name', '')

    form = NotiUpdateForm()

    return render(request, 'notification/add_update.html',
        {'form': form, 
        'client': client,
        'noti_type': noti_type,
        'ticket_no': ticket_no,
        'headline': headline,
        'requestor_name': requestor_name,
        })

def preview_email(request):
    client = request.GET.get('client', '')
    return render (request, 'notification/preview_email.html', {'client': client})



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


