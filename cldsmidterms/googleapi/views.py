from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from googleapiclient.discovery import build
from httplib2 import Http
from .models import Profile
from .forms import UserForm, ProfileForm, MailForm
import smtplib

# Create your views here.

@login_required
def Home(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            gmail_user = cd.get('gmail_user')
            gmail_pwd = cd.get('gmail_password')
            to = cd.get('to_email')
            subject = cd.get('subject')
            message = cd.get('message')
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + '\n'
            msg = header + '\n' + message + '\n\n'
            ##---------------email is sent ----------------##
            smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(gmail_user, gmail_pwd)
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()
            form = MailForm()
            context = {
                'form': form,
            }
            return render(request, 'home.html', context)
        else:
            # if sum not equal... then redirect to custom url/page
            return HttpResponseRedirect('/')  # mention redirect url in argument

    else:
        form = MailForm()  # blank form object just to pass context if not post method
        context = {
            'form': form,
        }

    return render(request, 'home.html', context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Maps(request):
    return render(request, 'maps.html')


