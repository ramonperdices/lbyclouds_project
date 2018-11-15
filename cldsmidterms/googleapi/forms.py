from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from googleapi.models import Profile
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')


class MailForm(forms.Form):
    gmail_user = forms.CharField()
    gmail_password = forms.CharField(widget=forms.PasswordInput)
    to_email = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()