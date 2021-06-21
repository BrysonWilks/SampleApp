from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def home(request):
    return render(request, 'home.html')


def validate(request):

    if request.method == 'POST':
        u_name = request.POST['username']
        p_word = request.POST['password']

        #Creating a user for test purposes
        U1 = models.User()
        U1.username = "Bob1234"
        U1.password = "password"

        if u_name == U1.username and p_word == U1.password:
            return render(request, 'userpage.html', {'username' : U1.username})
        else:
            messages.info(request, "Invalid user credentials")
            return redirect(home)
