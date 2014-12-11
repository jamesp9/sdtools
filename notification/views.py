from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.core.mail import send_mail

from .forms import StartNotificationForm,NotificationInformationForm,NotiUpdateForm


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

def start_notification(request):
    form = StartNotificationForm()

    return render(request, 'notification/start_notification.html', {'form': form})


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

    return render(request, 'notification/notification_information.html',
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


