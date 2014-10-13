from django import forms
from django.forms import ModelForm
from .models import QueryOptions




class EnterDataForm(ModelForm):
    class Meta:
        model QueryOptions
        fields = ['biginteger']
