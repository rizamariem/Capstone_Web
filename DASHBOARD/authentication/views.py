# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

from django.shortcuts import render
from core.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
import random
import string

#otp = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
#def otp_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))

def otp(size):
        
    # Takes random choices from
    # ascii_letters and digits
    generate_otp = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.digits)
                                            for n in range(size)])                           
    return generate_otp


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            raw_password = request.POST.get("password1")
            user = authenticate(username=username, password=raw_password)
            # form = User(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            subject = 'EmoBot Email Confirmation' 
            message = otp(6)
            recepient = request.POST.get("email")
            send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)

            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
