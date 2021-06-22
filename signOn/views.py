from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import models
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'home.html')


def validate(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'userpage.html', {'user':user})
        else:
            messages.info(request, "Invalid user credentials")
            return render(request, 'home.html')
