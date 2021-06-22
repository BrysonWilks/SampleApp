from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from .models import User, Book

# Create your views here.
def home(request):
    return render(request, 'home.html')


def validate(request):

    if request.method == 'POST':

        u_name = request.POST['username']
        p_word = request.POST['password']

        U1 = User.objects.all()

        for a in U1:
            if u_name == a.username and p_word == a.password:
                 return render(request, 'userpage.html', {'info' : U1})
        """
        if u_name in U1.username and p_word in U1.password:
            return render(request, 'userpage.html', {'info' : U1})
        else:
            messages.info(request, "Invalid user credentials")
            return redirect(home)
        """
