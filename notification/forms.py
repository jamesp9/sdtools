from django import forms

from .models import Notification, Update


class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['client', 'ntype', 'headline', 'ticket', 'raised', 'requester', ]


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update


# class NotificationInformationForm(forms.Form):
#     ticket_no = forms.CharField(max_length=100)
#     headline = forms.CharField(max_length=255)
#     requestor_name = forms.CharField(max_length=100)
