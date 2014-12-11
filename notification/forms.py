from django import forms

SUITE1_CLIENT_CHOICES = (
        ('client01', 'Client 01'), 
        ('client02', 'Client 02'), 
        ('client03', 'Client 03'),
        )

NOTIFICATION_CHOICES = (
        ('sev1', 'Severity 1'),
        ('hot_issue', 'Hot Issue'),
        )

class StartNotificationForm(forms.Form):
    client_name = forms.ChoiceField(label='Client', choices=SUITE1_CLIENT_CHOICES)
    noti_type = forms.ChoiceField(label='Notification', choices=NOTIFICATION_CHOICES)

class NotificationInformationForm(forms.Form):
    ticket_no = forms.CharField(max_length=100)
    headline = forms.CharField(max_length=255)
    requestor_name = forms.CharField(max_length=100)

class NotiUpdateForm(forms.Form):
    update_number = forms.IntegerField()
    update_time = forms.DateTimeField()
    update_person = forms.CharField(max_length=255)
    update_text = forms.CharField(widget=forms.Textarea)
    next_update_time = forms.DateTimeField()



